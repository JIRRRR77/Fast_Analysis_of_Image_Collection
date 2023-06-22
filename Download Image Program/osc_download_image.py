import osc_get_image_address
import urllib.request

# Download path
download_path_labeled = "/home/yiwei/Documents/New Fast Image Analysis/OSC_Split/Basic_set"
download_path_analysed = "/home/yiwei/Documents/New Fast Image Analysis/OSC_Split/Rest_set"


def download_image(all_image_url, download_path):
    for i in range(len(all_image_url)):
        # Adding information about user agent
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # Set up the image URL and filename
        image_url = all_image_url[i]
        filename = image_url.split("/")[-1]

        # if the image wasn't retrieved successfully, then skip
        try:
            # calling urlretrieve function to get resource
            urllib.request.urlretrieve(image_url, f"{download_path}/{filename}")
        except:
            pass


# Download image used for labeled
download_image(osc_get_image_address.all_image_url_labeled, download_path_labeled)

# Download image used for analysed
download_image(osc_get_image_address.all_image_url_analysed, download_path_analysed)
