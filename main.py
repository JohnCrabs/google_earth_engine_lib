import lib.my_calendar_v2 as my_cal_v2
import gee_lib.gee_lib as gee

_DATE_RANGE = ['2020-01-01', '2020-12-31']
_PERIOD_DAY_MULTIPLIER = 1  # days in a row
_PERIOD_ALPHA_MULTIPLIER = 1  # a multiplier for weeks
_PERIOD_STEP = _PERIOD_ALPHA_MULTIPLIER * _PERIOD_DAY_MULTIPLIER  # the period step

# Break the date range into smaller ranges
_LIST_DATE_RANGES_PERIOD = my_cal_v2.break_date_range_to_periods(date_start=_DATE_RANGE[0],
                                                                 date_end=_DATE_RANGE[1],
                                                                 period_step=_PERIOD_STEP,
                                                                 date_format=my_cal_v2.YYYY_MM_DD,
                                                                 date_delimeter=my_cal_v2.del_dash, century=21)

# Create a list with stings of the date range.
# e.g. ['2020-01-01', '2020-01-07'] => '20200101_20200107'
_LIST_DATE_RANGES_FOR_PATHS = my_cal_v2.create_string_list_date_range(list_input=_LIST_DATE_RANGES_PERIOD,
                                                                      del_input=my_cal_v2.del_dash,
                                                                      del_output=my_cal_v2.del_none)
# # Athens
# point_1 = [23.50, 37.75]
# point_2 = [24.00, 38.25]
# pixel_size = 50
#
# _EXPORT_NAME = 'S05_ATHENS_CO_'
# _FOLDER_NAME = 'S05_ATHENS_EUPOLIS'

# # Belgrade
# point_1 = [44.55, 20.20]
# point_2 = [45.05, 20.70]
# pixel_size = 50
#
# _EXPORT_NAME = 'S05_BELGRADE_CO_'
# _FOLDER_NAME = 'S05_BELGRADE_EUPOLIS'

# # Gladsaxe
# point_1 = [55.50, 12.25]
# point_2 = [56.00, 12.75]
# pixel_size = 50
#
# _EXPORT_NAME = 'S05_GLADSAXE_CO_'
# _FOLDER_NAME = 'S05_GLADSAXE_EUPOLIS'

# Lodz
point_1 = [51.50, 19.20]
point_2 = [52.00, 19.70]
pixel_size = 50

_EXPORT_NAME = 'S05_LODZ_CO_'
_FOLDER_NAME = 'S05_LODZ_EUPOLIS'

# # Rome
# point_1 = [41.65, 12.25]
# point_2 = [42.15, 12.75]
# pixel_size = 50
#
# _EXPORT_NAME = 'S05_ROME_CO_'
# _FOLDER_NAME = 'S05_ROME_EUPOLIS'


my_df = gee.GoogleEarthEngine()
dataset_code = gee.GSV_DS_SENTINEL_5_OFFL_CO_DKEY
band_name = [gee.DICT_FULL_DATASET[dataset_code][gee.BANDS_DKEY][gee.S05_CO_COLUMN_NUMBER_DENSITY_DKEY]]

for date_range_index in range(0, len(_LIST_DATE_RANGES_PERIOD)):
    my_df.set_collection_date_range(date_range=_LIST_DATE_RANGES_PERIOD[date_range_index])
    # my_df.set_collection_geometry_from_gee_country_str('Greece')
    my_df.set_collection_geometry_as_a_square_bound(point_1=point_1, point_2=point_2)
    my_df.set_collection(dataset_id=dataset_code)
    my_df.create_image_from_band(band_name[0])
    # my_df.create_image()
    export_name = _EXPORT_NAME + str(pixel_size) + '_' + _LIST_DATE_RANGES_FOR_PATHS[date_range_index]
    my_df.export_to_drive(export_name=export_name, scale_m2_px=pixel_size, folder_name=_FOLDER_NAME)
