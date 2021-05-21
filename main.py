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

point_1 = [23.00, 40.50]
point_2 = [23.25, 40.75]
pixel_size = 5

my_df = gee.GoogleEarthEngine()
dataset_code = gee.GSV_DS_SENTINEL_2_MSI_SR_DKEY
band_name = [gee.DICT_FULL_DATASET[dataset_code][gee.BANDS_DKEY][gee.RED_DKEY],
             gee.DICT_FULL_DATASET[dataset_code][gee.BANDS_DKEY][gee.GREEN_DKEY],
             gee.DICT_FULL_DATASET[dataset_code][gee.BANDS_DKEY][gee.BLUE_DKEY]]

for date_range_index in range(0, len(_LIST_DATE_RANGES_PERIOD)):
    my_df.set_collection_date_range(date_range=_LIST_DATE_RANGES_PERIOD[date_range_index])
    # my_df.set_collection_geometry_from_gee_country_str('Greece')
    my_df.set_collection_geometry_as_a_square_bound(point_1=point_1, point_2=point_2)
    my_df.set_collection(dataset_id=dataset_code)
    my_df.create_image()
    export_name = 'S02_EGNATIA_' + str(pixel_size) + '_' + _LIST_DATE_RANGES_FOR_PATHS[date_range_index]
    my_df.export_to_drive(export_name=export_name, scale_m2_px=pixel_size, folder_name='PANOPTIS_EGNATIA')
