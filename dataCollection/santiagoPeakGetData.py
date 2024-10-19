import requests

# URL of the image you want to download
count = 0;

for i in range(1729349997, 1729359124):
	

    image_url = f'https://cameras.alertcalifornia.org/public-camera-data/Axis-SantiagoPeakCalOESN/1min/{i}.000000000.jpg'

    # Local file path where you want to save the image
    save_path = f'./data/santiagoPeakNoFire/img{i}.jpg'

    # Send a GET request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(count)
        # Open the file in write-binary mode and save the image
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    else:
        count += 1
        print(f"Failed to download image. Status code: {response.status_code}")

