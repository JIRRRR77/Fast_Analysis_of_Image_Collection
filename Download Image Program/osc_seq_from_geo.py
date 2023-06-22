import requests

baseurl = 'https://api.openstreetcam.org/2.0/'


# Generate the related sequences based on latitude and longitude coordinate
def sequence_of_photo(lat, lng):
    # Temporary list for sequence id storage
    sequence_id = []

    for i, j in zip(lat, lng):
        # Create geo-endpoint based on latitude and longitude coordinate
        geo_endpoint = 'photo?lat=' + str(i) + '&lng=' + str(j)
        print(geo_endpoint)

        # Get the information of the image
        r = requests.get(baseurl + geo_endpoint)
        photo_info = r.json()

        # Retrieve the sequence id from image's information
        for k in range(len(photo_info['result']['data'])):
            sequence_id.append(photo_info['result']['data'][k]['sequenceId'])

    # Remove Duplicates in Sequence id
    new_sequence_id = list(set(sequence_id))
    print('It will retrieve ' + str(len(new_sequence_id)) + ' sequence id. \n')
    return new_sequence_id


# The latitude and longitude coordinate used for 5% labeled images.
lat_for_labeled = [52.614736]
lng_for_labeled = [13.248063]
print('For labeled photos:')
new_seq_id_labeled = sequence_of_photo(lat_for_labeled, lng_for_labeled)

# The latitude and longitude coordinates used for 95% analysed images.
lat_for_analysis = [52.515718, 52.52074051, 52.47871399]
lng_for_analysis = [13.369948, 13.41519642, 13.34378815]
print('For analysed photos:')
new_seq_id_analysis = sequence_of_photo(lat_for_analysis, lng_for_analysis)
