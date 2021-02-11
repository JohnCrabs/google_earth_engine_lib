import gee_lib.gee_lib as gee

list_country = ['Canada', 'Greece']

my_df = gee.GoogleEarthEngine()
my_df.set_collection_date_range(date_range=['1975-07-23T00:00:00', '1975-07-30T00:00:00'])
my_df.set_collection_geometry_from_gee_country_list(list_country=list_country)
# my_df.prt_image_geometry()
my_df.set_collection(gee.GSV_DS_LANDSAT_1_COLLECTION_ID)
# my_df.prt_image_collection()
my_df.create_image_form_collection_mean()
my_df.export_to_Drive()
