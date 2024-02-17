import datetime
import cv2
import easyocr
import math

from PIL import Image, ImageDraw

from config_module import config
screenshots_path = config.screenshots_path
output_path = config.output_path
element_ss_path = config.element_ss_path

def _perform_ocr():
    global results, image, time_delta
    image = cv2.imread(screenshots_path)
    time_initial = datetime.datetime.now()
    reader = easyocr.Reader(
        ['en'],
        gpu=True
    )

    # Perform OCR on the image
    print('reading text from webpage...')
    results = reader.readtext(image, batch_size=64, slope_ths=0.5)
    time_delta = datetime.datetime.now() - time_initial
    time_delta = str(time_delta)[:-4]
    print(f"time took to read all the text from webpage- {time_delta}")

def _analyse_ocr_results(txtToSearch, exactmatch, item_position, top_leftRX=-1, midpointRY=-1, y_axis=False):
    #time_initial = datetime.datetime.now()
    listValues = []
    list_top = []
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        top_leftX = top_left[0]
        top_leftY = top_left[1]
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
                        topleft = top_leftX, top_leftY
                        list_top.append(topleft)
                elif not midpointRY == -1:
                    #print(f'in == top_left diff of {midpointRY},{midpointY}=={abs(midpointRY - midpointY)}')
                    if abs(midpointRY - midpointY) <= 10:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                        topleft = top_leftX, top_leftY
                        list_top.append(topleft)
                else:
                    midpoint = midpointX, midpointY
                    top_left_found = top_leftX
                    listValues.append(midpoint)
                    topleft = top_leftX, top_leftY
                    list_top.append(topleft)
        else:
            if txtToSearch.lower() in text.lower():
                #print(f'{text} -- {midpointX},{midpointY} top_leftX --{top_leftX}')
                if not top_leftRX == -1:
                    #print(f'in == top_left diff of {top_leftRX},{top_leftX}=={abs(top_leftRX - top_leftX)}')
                    if abs(top_leftRX - top_leftX) < 5:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                        topleft = top_leftX, top_leftY
                        list_top.append(topleft)
                elif not midpointRY == -1:
                    #print(f'in == top_left diff of {midpointRY},{midpointY}=={abs(midpointRY - midpointY)}')
                    if abs(midpointRY - midpointY) < 5:
                        midpoint = midpointX, midpointY
                        listValues.append(midpoint)
                        topleft = top_leftX, top_leftY
                        list_top.append(topleft)
                else:
                    midpoint = midpointX, midpointY
                    top_left_found = top_leftX
                    listValues.append(midpoint)
                    topleft = top_leftX, top_leftY
                    list_top.append(topleft)
                    # Draw a bounding box around the detected text
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        # print(f'Bounding Box Coordinates:{text}, {top_left}, {bottom_right}')

    cv2.imwrite(output_path, image)
    distances = [math.sqrt(x ** 2 + y ** 2) for x, y in listValues]
    distances_tl = [math.sqrt(a ** 2 + b ** 2) for a, b in list_top]

    # Create a list of (distance, coordinate) pairs
    distance_coordinate_pairs = list(zip(distances, listValues))
    distance_coordinate_pairs_tl = list(zip(distances_tl, list_top))
    # Sort the pairs by distance in ascending order
    sorted_pairs = sorted(distance_coordinate_pairs, key=lambda x: x[0])
    sorted_pairs_tl = sorted(distance_coordinate_pairs_tl, key=lambda a: a[0])

    # Extract the sorted coordinates
    sorted_coordinates = [pair[1] for pair in sorted_pairs]
    sorted_coordinates_tl = [pair[1] for pair in sorted_pairs_tl]
    top_left_x, top_left_y = sorted_coordinates_tl[item_position-1]
    midpoint_x, midpoint_y = sorted_coordinates[item_position-1]
    bottom_right_x = 2 * midpoint_x - top_left_x
    bottom_right_y = 2 * midpoint_y - top_left_y
    top_left = top_left_x, top_left_y
    bottom_right = bottom_right_x, bottom_right_y
    coordinates = top_left_x, top_left_y, bottom_right_x, bottom_right_y
    #time_delta = datetime.datetime.now() - time_initial
    #print(f"Time took to analyse - {time_delta}")
    #cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
    #cv2.imwrite(output_path, image)
    ss = Image.open(screenshots_path)
    draw = ImageDraw.Draw(ss)
    draw.rectangle(coordinates, outline="red", width=3)
    ss.save(element_ss_path)


    if y_axis:
        return top_left_found
    else:
        return sorted_coordinates[item_position-1]
