from datetime import datetime
from config_module import config
screenshots_folder = config.screenshots_folder
rows = ""

def generate_html():
        global rows
        # Get current date and time
        current_datetime = datetime.now()
        # Format date and time as dd-mmm-yyyy hh:mm:ss
        formatted_datetime = current_datetime.strftime("%d-%b-%Y %H:%M:%S")
        html_content = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>HTML Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
        
                table {{
                    width: 70%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
        
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
        
                th {{
                    background-color: #f2f2f2;
                }}
        
                tr {{
                    height: 100px;
                }}

        
                img {{
                    max-width: 50%;
                    height: auto;
                    cursor: grab
                }}
                #imageModal {{
                    display: none;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0, 0, 0, 0.7);
                    justify-content: center;
                    align-item_positions: center;
                }}

                #modalContent {{
                    text-align: center;
                }}
        
                #modalImage {{
                    max-width: 80%;
                    max-height: 80%;
                    border: 2px solid #fff;
                    border-radius: 5px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
            </style>
            <script>
        function openImageModal(imageSrc) {{
            var modal = document.getElementById('imageModal');
            var modalImg = document.getElementById('modalImage');
            modalImg.src = imageSrc;
            modal.style.display = 'flex';
            }}

        function closeImageModal() {{
            document.getElementById('imageModal').style.display = 'none';
        }}
    </script>
        </head>
        <body>
        
        <h1>HTML Report</h1>
        <h3>Date: {formatted_datetime} Hrs</h3>        
        <table>
            <tr>
                <th width="50%">Step</th>
                <th width="10%">Result</th>
                <th width="10%">Time Taken</th>
                <th width="30%">Screenshot</th>
            </tr>
            {rows}
        </table>
          <div id="imageModal" onclick="closeImageModal()">
            <div id="modalContent">
                <img id="modalImage" src="" alt="Modal Image">
            </div>
        </div>
        </body>
        </html>
        """
        return html_content
def report(step, status, time_delta, screenshot):
    global rows
    if status == "Failed":
       color = "#F2938C"
    else:
       color = "#46C646"
    rows += f"""
        <tr>
        <td>{step}</td>
        <td style="color: {color}; font-weight: bold">{status}</td>
         <td>{time_delta}</td>
        <td><img src='../{screenshot}' alt="Screenshot" onclick="openImageModal('../{screenshot}')"></td>
        </tr>
        """
    with open(screenshots_folder + '/output.html', 'w') as file:
        file.write(generate_html())
    #print(f"rows {rows}")