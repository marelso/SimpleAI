from google_images_search import GoogleImagesSearch as externalApi


def search_image(image_to_search):
    # Use a breakpoint in the code line below to debug your script.
    gis = externalApi('api_key', 'cx')
    gis.search({'q': 'bookshelf', 'num': 10})


if __name__ == '__main__':
    search_image('PyCharm')