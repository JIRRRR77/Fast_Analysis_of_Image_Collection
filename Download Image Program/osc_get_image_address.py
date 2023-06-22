import requests
import osc_seq_from_geo


# Generate photo's endpoint with selected pages and items per page
def retrieve_photo_endpoint(sequence_id, pages, items_per_page):
    eps = []
    for page in range(1, pages + 1):
        ep = 'sequence/' + sequence_id + '/photos?page=' + str(page) + '&itemsPerPage=' + str(items_per_page)
        eps.append(ep)
    return eps


# Use photos' endpoints to generate all photos' url
def url_of_photo(endpoints):
    # returned list for photos' url storage
    all_image_address = []

    for endpoint in endpoints:
        # Get the information of the photo's sequence
        r = requests.get(osc_seq_from_geo.baseurl + endpoint)
        data = r.json()

        # Temporary list for photos' url storage
        image_address = []

        # if the image's url wasn't retrieved successfully, then skip
        try:
            for i in range(len(data['result']['data'])):
                image_address.append(data['result']['data'][i]['fileurlLTh'])
        except:
            pass
        # Add temporary list's content into returned list's content
        all_image_address.extend(image_address)

        # Print the number of photos' url in each page of each sequence
        print('In sequenceId: ' + endpoint.split('/')[1] + ' page: ' + endpoint.split('&')[0].split('=')[
            1] + ', you get ' + str(len(image_address)) + ' images.')

    # Print the total number of photos' url.
    print('It will retrieve ' + str(len(all_image_address)) + ' images. \n')
    return all_image_address


# Get image url used for labeled
Pages_labeled = int(input("Please enter the total pages you wished for labeled(default = 1): ") or 1)
itemsPerPage_labeled = int(input("Please enter items per page you wished for labeled(default = 100): ") or 100)

endpoints_labeled = []
for sequenceId in osc_seq_from_geo.new_seq_id_labeled:
    endpoints_labeled.extend(retrieve_photo_endpoint(sequenceId, Pages_labeled, itemsPerPage_labeled))
print('For labeled photos:')
all_image_url_labeled = url_of_photo(endpoints_labeled)

# Get image url used for analysed
Pages_analysed = int(input("Please enter the total pages you wished for analysed(default = 2): ") or 2)
itemsPerPage_analysed = int(input("Please enter items per page you wished for analysed(default = 100): ") or 100)

endpoints_analysed = []
for sequenceId in osc_seq_from_geo.new_seq_id_analysis:
    endpoints_analysed.extend(retrieve_photo_endpoint(sequenceId, Pages_analysed, itemsPerPage_analysed))
print('For analysed photos:')
all_image_url_analysed = url_of_photo(endpoints_analysed)
