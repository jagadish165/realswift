import datetime
import os
import cv2
import easyocr
import math
from config_module import config
screenshot_path = config.screenshot_path
output_path = config.output_path

def _perform_ocr():
    global results, image
    image = cv2.imread(screenshot_path)
    time_initial = datetime.datetime.now()
    reader = easyocr.Reader(
        ['en'],
        gpu=True
    )

    # Perform OCR on the image
    print('Reading text from screenshot........')
    results = reader.readtext(image, batch_size=64, slope_ths=0.5)
    time_delta = datetime.datetime.now() - time_initial
    print(f"Time took to read - {time_delta}")

def _analyse_ocr_results(txtToSearch, exactmatch, item, top_leftRX=-1, midpointRY=-1, y_axis=False):
    #time_initial = datetime.datetime.now()
    listValues = []
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        top_leftX = top_left[0]
        midpointX = (top_left[0] + bottom_right[0]) // 2
        midpointY = (top_left[1] + bottom_right[1]) // 2
        if exactmatch:
            if text.lower() == txtToSearch.lower():
                #print(f'{text} -- {midpointX},{midpointY} top_leftX --{top_leftX}')
                if not top_leftRX == -1:
                    #print(f'in == top_left diff of {top_leftRX},{top_leftX}=={abs(top_leftRX - top_leftX)}')
                    if abs(top_leftRX - top_leftX) <= 10:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                elif not midpointRY == -1:
                    #print(f'in == top_left diff of {midpointRY},{midpointY}=={abs(midpointRY - midpointY)}')
                    if abs(midpointRY - midpointY) <= 10:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                else:
                    midpoint = midpointX, midpointY
                    top_left_found = top_leftX
                    listValues.append(midpoint)
        else:
            if txtToSearch.lower() in text.lower():
                #print(f'{text} -- {midpointX},{midpointY} top_leftX --{top_leftX}')
                if not top_leftRX == -1:
                    #print(f'in == top_left diff of {top_leftRX},{top_leftX}=={abs(top_leftRX - top_leftX)}')
                    if abs(top_leftRX - top_leftX) < 5:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                elif not midpointRY == -1:
                    #print(f'in == top_left diff of {midpointRY},{midpointY}=={abs(midpointRY - midpointY)}')
                    if abs(midpointRY - midpointY) < 5:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                else:
                    midpoint = midpointX, midpointY
                    top_left_found = top_leftX
                    listValues.append(midpoint)
                    # Draw a bounding box around the detected text
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        # print(f'Bounding Box Coordinates:{text}, {top_left}, {bottom_right}')

    try:
        now = datetime.datetime.now()
        new_file_name = f"output_{now.strftime('%Y-%m-%d-%H-%M-%S')}.png"
        os.rename(output_path, f"target/old_ss/{new_file_name}")
    except Exception as e:
        print(f"exception {e}")
    cv2.imwrite(output_path, image)
    distances = [math.sqrt(x ** 2 + y ** 2) for x, y in listValues]
    # Create a list of (distance, coordinate) pairs
    distance_coordinate_pairs = list(zip(distances, listValues))

    # Sort the pairs by distance in ascending order
    sorted_pairs = sorted(distance_coordinate_pairs, key=lambda x: x[0])

    # Extract the sorted coordinates
    sorted_coordinates = [pair[1] for pair in sorted_pairs]

    print(f'{txtToSearch} = {sorted_coordinates}')
    #time_delta = datetime.datetime.now() - time_initial
    #print(f"Time took to analyse - {time_delta}")
    if y_axis:
        return top_left_found
    else:
        return sorted_coordinates[item]
