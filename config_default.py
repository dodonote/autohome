#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'daidai'

configs = dict()
configs = {
    'full_type_name':{'name': u'车型名称', 'field': 'full_type_name'},
    'firm_price':{'name': u'厂商指导价(元)', 'field': 'firm_price'},
    'firm':{'name': u'厂商', 'field': 'firm'},
    'grade':{'name': u'级别', 'field': 'grade'},
    'engine':{'name': u'发动机', 'field': 'engine'},
    'gear_box':{'name': u'变速箱', 'field': 'gear_box'},
    'cubage':{'name': u'长*宽*高(mm)', 'field': 'cubage'},
    'detail_body_structure':{'name': u'车身结构', 'field': 'detail_body_structure'},
    'max_speed':{'name': u'最高车速(km/h)', 'field': 'max_speed'},
    'official_acceleration':{'name': u'官方0-100km/h加速(s)', 'field': 'official_acceleration'},
    'measure_acceleration':{'name': u'实测0-100km/h加速(s)', 'field': 'measure_acceleration'},
    'measure_brake':{'name': u'实测100-0km/h制动(m)', 'field': 'measure_brake'},
    'measure_fuel_consumption':{'name': u'实测油耗(L/100km)', 'field': 'measure_fuel_consumption'},
    'combine_fuel_consumption':{'name': u'工信部综合油耗(L/100km)', 'field': 'combine_fuel_consumption'},
    'vehicle_warranty':{'name': u'整车质保', 'field': 'vehicle_warranty'},
    'car_length':{'name': u'长度(mm)', 'field': 'car_length'},
    'car_width':{'name': u'宽度(mm)', 'field': 'car_width'},
    'car_height':{'name': u'高度(mm)', 'field': 'car_height'},
    'wheelbase':{'name': u'轴距(mm)', 'field': 'wheelbase'},
    'front_track':{'name': u'前轮距(mm)', 'field': 'front_track'},
    'rear_track':{'name': u'后轮距(mm)', 'field': 'rear_track'},
    'min_ground_clearance':{'name': u'最小离地间隙(mm)', 'field': 'min_ground_clearance'},
    'curb_weight':{'name': u'整备质量(kg)', 'field': 'curb_weight'},
    'body_structure':{'name': u'车身结构', 'field': 'body_structure'},
    'door_number':{'name': u'车门数(个)', 'field': 'door_number'},
    'seat_number':{'name': u'座位数(个)', 'field': 'seat_number'},
    'tank_capacity':{'name': u'油箱容积(L)', 'field': 'tank_capacity'},
    'luggage_volume':{'name': u'行李厢容积(L)', 'field': 'luggage_volume'},
    'engine_model':{'name': u'发动机型号', 'field': 'engine_model'},
    'emission':{'name': u'排量(mL)', 'field': 'emission'},
    'emission_liter':{'name': u'排量(L)', 'field': 'emission_liter'}, # 已删除
    'intake_form':{'name': u'进气形式', 'field': 'intake_form'},
    'cylinder_arrange':{'name': u'气缸排列形式', 'field': 'cylinder_arrange'},
    'cylinder_number':{'name': u'气缸数(个)', 'field': 'cylinder_number'},
    'cylinder_valve':{'name': u'每缸气门数(个)', 'field': 'cylinder_valve'},
    'compression_ratio':{'name': u'压缩比', 'field': 'compression_ratio'},
    'air_supply':{'name': u'配气机构', 'field': 'air_supply'},
    'bore':{'name': u'缸径(mm)', 'field': 'bore'},
    'stroke':{'name': u'行程(mm)', 'field': 'stroke'},
    'max_horsepower':{'name': u'最大马力(Ps)', 'field': 'max_horsepower'},
    'max_power':{'name': u'最大功率(kW)', 'field': 'max_power'},
    'max_power_speed':{'name': u'最大功率转速(rpm)', 'field': 'max_power_speed'},
    'max_torque':{'name': u'最大扭矩(N·m)', 'field': 'max_torque'},
    'max_torque_speed':{'name': u'最大扭矩转速(rpm)', 'field': 'max_torque_speed'},
    'engine_specific_technology':{'name': u'发动机特有技术', 'field': 'engine_specific_technology'},
    'fuel_form':{'name': u'燃料形式', 'field': 'fuel_form'},
    'fuel_grade':{'name': u'燃油标号', 'field': 'fuel_grade'},
    'fuel_supply_means':{'name': u'供油方式', 'field': 'fuel_supply_means'},
    'cylinder_material':{'name': u'缸盖材料', 'field': 'cylinder_material'},
    'block_material':{'name': u'缸体材料', 'field': 'block_material'},
    'environment_standards':{'name': u'环保标准', 'field': 'environment_standards'},
    'max_motor_power':{'name': u'电动机最大功率(kW)', 'field': 'max_motor_power'}, # 已删除
    'max_motor_torque':{'name': u'电动机最大扭矩(N·m)', 'field': 'max_motor_torque'}, # 已删除
    'battery_support_mileage':{'name': u'电池支持最高续航里程(km)', 'field': 'battery_support_mileage'}, # 已删除
    'abbreviation':{'name': u'简称', 'field': 'abbreviation'},
    'gear_number':{'name': u'挡位个数', 'field': 'gear_number'},
    'gearbox_type':{'name': u'变速箱类型', 'field': 'gearbox_type'},
    'drive_mode':{'name': u'驱动方式', 'field': 'drive_mode'},
    'four_wheel_drive_form':{'name': u'四驱形式', 'field': 'four_wheel_drive_form'}, # 已删除
    'center_diff_structure':{'name': u'中央差速器结构', 'field': 'center_diff_structure'}, # 已删除
    'front_suspension_type':{'name': u'前悬架类型', 'field': 'front_suspension_type'},
    'rear_suspension_type':{'name': u'后悬架类型', 'field': 'rear_suspension_type'},
    'booster_type':{'name': u'助力类型', 'field': 'booster_type'},
    'chassis_body_structure':{'name': u'车体结构', 'field': 'chassis_body_structure'},
    'front_brake_type':{'name': u'前制动器类型', 'field': 'front_brake_type'},
    'rear_brake_type':{'name': u'后制动器类型', 'field': 'rear_brake_type'},
    'parking_brake_type':{'name': u'驻车制动类型', 'field': 'parking_brake_type'},
    'front_tire_specification':{'name': u'前轮胎规格', 'field': 'front_tire_specification'},
    'tear_tire_specification':{'name': u'后轮胎规格', 'field': 'tear_tire_specification'},
    'spare_tire_specification':{'name': u'备胎规格', 'field': 'spare_tire_specification'},
    'main_airbag':{'name': u'驾驶座安全气囊', 'field': 'main_airbag'}, # 已删除
    'sub_airbag':{'name': u'副驾驶安全气囊', 'field': 'sub_airbag'}, # 已删除
    'main_sub_airbag':{'name': u'主/副驾驶座安全气囊', 'field': 'main_sub_airbag'},
    'front_side_airbag':{'name': u'前排侧气囊', 'field': 'front_side_airbag'}, # 已删除
    'rear_side_airbag':{'name': u'后排侧气囊', 'field': 'rear_side_airbag'}, # 已删除
    'front_rear_side_airbag':{'name': u'前/后排侧气囊', 'field': 'front_rear_side_airbag'}, # 已删除
    'front_head_airbag':{'name': u'前排头部气囊(气帘)', 'field': 'front_head_airbag'}, # 已删除
    'rear_head_airbag':{'name': u'后排头部气囊(气帘)', 'field': 'rear_head_airbag'}, # 已删除
    'front_rear_head_airbag':{'name': u'前/后排头部气囊(气帘)', 'field': 'front_rear_head_airbag'},
    'knee_airbag':{'name': u'膝部气囊', 'field': 'knee_airbag'},
    'tire_pressure_monitor_device':{'name': u'胎压监测装置', 'field': 'tire_pressure_monitor_device'},
    'zero_tire_pressure_trave':{'name': u'零胎压继续行驶', 'field': 'zero_tire_pressure_trave'},
    'seat_belt_prompt':{'name': u'安全带未系提示', 'field': 'seat_belt_prompt'},
    'isofix_child_seat_interface':{'name': u'ISOFIX儿童座椅接口', 'field': 'isofix_child_seat_interface'},
    'latch_seat_interface':{'name': u'LATCH座椅接口(兼容ISOFIX)', 'field': 'latch_seat_interface'}, # 已删除
    'child_seat_interface':{'name': u'儿童座椅接口', 'field': 'child_seat_interface'}, # 已删除
    'electronic_anti_theft':{'name': u'发动机电子防盗', 'field': 'electronic_anti_theft'},
    'car_central_lock':{'name': u'车内中控锁', 'field': 'car_central_lock'},
    'remote_key':{'name': u'遥控钥匙', 'field': 'remote_key'},
    'keyless_start_system':{'name': u'无钥匙启动系统', 'field': 'keyless_start_system'},
    'keyless_entry_system':{'name': u'无钥匙进入系统', 'field': 'keyless_entry_system'},
    'abs_anti_lock':{'name': u'ABS防抱死', 'field': 'abs_anti_lock'},
    'brake_force_distribution':{'name': u'制动力分配(EBD/CBC等)', 'field': 'brake_force_distribution'},
    'brake_assist':{'name': u'刹车辅助(EBA/BAS/BA等)', 'field': 'brake_assist'},
    'traction_control':{'name': u'牵引力控制(ASR/TCS/TRC等)', 'field': 'traction_control'},
    'vehicle_stability_control':{'name': u'车身稳定控制(ESC/ESP/DSC等)', 'field': 'vehicle_stability_control'},
    'automatic_parking':{'name': u'自动驻车', 'field': 'automatic_parking'},
    'hill_descent':{'name': u'陡坡缓降', 'field': 'hill_descent'},
    'variable_suspension':{'name': u'可变悬架', 'field': 'variable_suspension'},
    'air_suspension':{'name': u'空气悬架', 'field': 'air_suspension'},
    'variable_steer_ratio':{'name': u'可变转向比', 'field': 'variable_steer_ratio'},
    'front_axle_limited_slip':{'name': u'前桥限滑差速器/差速锁', 'field': 'front_axle_limited_slip'},
    'center_lock_function':{'name': u'中央差速器锁止功能', 'field': 'center_lock_function'},
    'tear_axle_limited_slip':{'name': u'后桥限滑差速器/差速锁', 'field': 'tear_axle_limited_slip'},
    'electric_sunroof':{'name': u'电动天窗', 'field': 'electric_sunroof'},
    'panoramic_sunroof':{'name': u'全景天窗', 'field': 'panoramic_sunroof'},
    'sport_package':{'name': u'运动外观套件', 'field': 'sport_package'},
    'alloy_wheels':{'name': u'铝合金轮毂', 'field': 'alloy_wheels'},
    'electric_door':{'name': u'电动吸合门', 'field': 'electric_door'},
    'leather_wheel':{'name': u'真皮方向盘', 'field': 'leather_wheel'},
    'steering_wheel_up_and_down':{'name': u'方向盘上下调节', 'field': 'steering_wheel_up_and_down'}, # 已删除
    'steering_wheel_before_and_after':{'name': u'方向盘前后调节', 'field': 'steering_wheel_before_and_after'}, # 已删除
    'steering_wheel_adjust':{'name': u'方向盘调节', 'field': 'steering_wheel_adjust'},
    'steering_wheel_electronic_adjust':{'name': u'方向盘电动调节', 'field': 'steering_wheel_electronic_adjust'},
    'multi_steering_wheel':{'name': u'多功能方向盘', 'field': 'multi_steering_wheel'},
    'steering_wheel_shift':{'name': u'方向盘换挡', 'field': 'steering_wheel_shift'},
    'steering_wheel_heat':{'name': u'方向盘加热', 'field': 'steering_wheel_heat'},
    'cruise_control':{'name': u'定速巡航', 'field': 'cruise_control'},
    'former_radar':{'name': u'前驻车雷达', 'field': 'former_radar'}, # 已删除
    'after_reversing_radar':{'name': u'后驻车雷达', 'field': 'after_reversing_radar'}, # 已删除
    'former_after_radar':{'name': u'前/后驻车雷达', 'field': 'former_after_radar'},
    'reversing_video':{'name': u'倒车视频影像', 'field': 'reversing_video'},
    'trip_computer_display':{'name': u'行车电脑显示屏', 'field': 'trip_computer_display'},
    'head_up_digital_display':{'name': u'HUD抬头数字显示', 'field': 'head_up_digital_display'},
    'leather_seat':{'name': u'座椅材质', 'field': 'leather_seat'},
    'sports_style_seat':{'name': u'运动风格座椅', 'field': 'sports_style_seat'},
    'seat_height_adjust':{'name': u'座椅高低调节', 'field': 'seat_height_adjust'},
    'lumbar_support_adjust':{'name': u'腰部支撑调节', 'field': 'lumbar_support_adjust'},
    'shoulder_support_adjust':{'name': u'肩部支撑调节', 'field': 'shoulder_support_adjust'},
    'driving_position_electric_adjust':{'name': u'驾驶位电动调节', 'field': 'driving_position_electric_adjust'}, # 已删除
    'copilot_electric_adjust':{'name': u'副驾驶位电动调节', 'field': 'copilot_electric_adjust'}, # 已删除
    'main_sub_electric_adjust':{'name': u'主/副驾驶座电动调节', 'field': 'main_sub_electric_adjust'},
    'second_row_angle_adjust':{'name': u'第二排靠背角度调节', 'field': 'second_row_angle_adjust'},
    'second_row_seat_move':{'name': u'第二排座椅移动', 'field': 'second_row_seat_move'},
    'rear_seat_electric_adjust':{'name': u'后排座椅电动调节', 'field': 'rear_seat_electric_adjust'},
    'electric_seat_memory':{'name': u'电动座椅记忆', 'field': 'electric_seat_memory'},
    'front_seat_heat':{'name': u'前排座椅加热', 'field': 'front_seat_heat'}, # 已删除
    'rear_seat_heat':{'name': u'后排座椅加热', 'field': 'rear_seat_heat'}, # 已删除
    'front_rear_seat_heat':{'name': u'前/后排座椅加热', 'field': 'front_rear_seat_heat'},
    'front_seat_ventilation':{'name': u'前排座椅通风', 'field': 'front_seat_ventilation'}, # 已删除
    'rear_seat_ventilation':{'name': u'后排座椅通风', 'field': 'rear_seat_ventilation'}, # 已删除
    'front_rear_seat_ventilation':{'name': u'前/后排座椅通风', 'field': 'front_rear_seat_ventilation'},
    'front_seat_massage':{'name': u'前排座椅按摩', 'field': 'front_seat_massage'}, # 已删除
    'rear_seat_massage':{'name': u'后排座椅按摩', 'field': 'rear_seat_massage'}, # 已删除
    'front_rear_seat_massage':{'name': u'前/后排座椅按摩', 'field': 'front_rear_seat_massage'},
    'rear_seat_overall_recline':{'name': u'后排座椅整体放倒', 'field': 'rear_seat_overall_recline'}, # 已删除
    'rear_seat_proportion_recline':{'name': u'后排座椅比例放倒', 'field': 'rear_seat_proportion_recline'}, # 已删除
    'rear_seat_recline':{'name': u'后排座椅放倒方式', 'field': 'rear_seat_recline'},
    'third_row_seat':{'name': u'第三排座椅', 'field': 'third_row_seat'},
    'front_seat_center_armrest':{'name': u'前座中央扶手', 'field': 'front_seat_center_armrest'}, # 已删除
    'rear_seat_center_armrest':{'name': u'后座中央扶手', 'field': 'rear_seat_center_armrest'}, # 已删除
    'front_rear_seat_center_armrest':{'name': u'前/后中央扶手', 'field': 'front_rear_seat_center_armrest'},
    'rear_cup_holders':{'name': u'后排杯架', 'field': 'rear_cup_holders'},
    'electric_trunk':{'name': u'电动后备厢', 'field': 'electric_trunk'}, # 已删除
    'gps_navigation_system':{'name': u'GPS导航系统', 'field': 'gps_navigation_system'},
    'position_interactive_service':{'name': u'定位互动服务', 'field': 'position_interactive_service'},
    'center_console_screen':{'name': u'中控台彩色大屏', 'field': 'center_console_screen'},
    'human_computer_interaction_system':{'name': u'人机交互系统', 'field': 'human_computer_interaction_system'}, # 已删除
    'built_in_hard_drive':{'name': u'内置硬盘', 'field': 'built_in_hard_drive'}, # 已删除
    'bluetooth':{'name': u'蓝牙/车载电话', 'field': 'bluetooth'},
    'car_tv':{'name': u'车载电视', 'field': 'car_tv'},
    'rear_lcd_screen':{'name': u'后排液晶屏', 'field': 'rear_lcd_screen'},
    'external_audio_interface':{'name': u'外接音源接口', 'field': 'external_audio_interface'},
    'support_mp3':{'name': u'CD支持MP3/WMA', 'field': 'support_mp3'},
    'single_disc_cd':{'name': u'单碟CD', 'field': 'single_disc_cd'}, # 已删除
    'virtual_multi_disc_cd':{'name': u'虚拟多碟CD', 'field': 'virtual_multi_disc_cd'}, # 已删除
    'multi_disc_cd_system':{'name': u'多碟CD系统', 'field': 'multi_disc_cd_system'}, # 已删除
    'cd_system':{'name': u'CD系统', 'field': 'cd_system'}, # 已删除
    'single_disc_dvd':{'name': u'单碟DVD', 'field': 'single_disc_dvd'}, # 已删除
    'multi_disc_dvd_system':{'name': u'多碟DVD系统', 'field': 'multi_disc_dvd_system'}, # 已删除
    'dvd_system':{'name': u'DVD系统', 'field': 'dvd_system'}, # 已删除
    'mutlti_system':{'name': u'多媒体系统', 'field': 'mutlti_system'},
    'horn_speaker_system1':{'name': u'2-3喇叭扬声器系统', 'field': 'horn_speaker_system1'}, # 已删除
    'horn_speaker_system2':{'name': u'4-5喇叭扬声器系统', 'field': 'horn_speaker_system2'}, # 已删除
    'horn_speaker_system3':{'name': u'6-7喇叭扬声器系统', 'field': 'horn_speaker_system3'}, # 已删除
    'horn_speaker_system4':{'name': u'≥8喇叭扬声器系统', 'field': 'horn_speaker_system4'}, # 已删除
    'horn_speaker_num':{'name': u'扬声器数量', 'field': 'horn_speaker_num'},
    'xenon_headlight':{'name': u'氙气大灯', 'field': 'xenon_headlight'}, # 已删除
    'led_headlamp':{'name': u'LED大灯', 'field': 'led_headlamp'}, # 已删除
    'daytime_running_light':{'name': u'日间行车灯', 'field': 'daytime_running_light'},
    'automatic_headlight':{'name': u'自动头灯', 'field': 'automatic_headlight'},
    'steering_headlight':{'name': u'转向头灯', 'field': 'steering_headlight'},
    'front_fog_lamp':{'name': u'前雾灯', 'field': 'front_fog_lamp'},
    'height_adjust_headlight':{'name': u'大灯高度可调', 'field': 'height_adjust_headlight'},
    'headlight_clean_system':{'name': u'大灯清洗装置', 'field': 'headlight_clean_system'},
    'ambient_light':{'name': u'车内氛围灯', 'field': 'ambient_light'},
    'front_electric_windows':{'name': u'前电动车窗', 'field': 'front_electric_windows'}, # 已删除
    'rear_power_windows':{'name': u'后电动车窗', 'field': 'rear_power_windows'}, # 已删除
    'front_rear_power_windows':{'name': u'前/后电动车窗', 'field': 'front_rear_power_windows'},
    'window_fangga_hand':{'name': u'车窗防夹手功能', 'field': 'window_fangga_hand'},
    'insulated_glass':{'name': u'防紫外线/隔热玻璃', 'field': 'insulated_glass'},
    'rear_mirror_adjust':{'name': u'后视镜电动调节', 'field': 'rear_mirror_adjust'},
    'rear_mirror_heat':{'name': u'后视镜加热', 'field': 'rear_mirror_heat'},
    'inside_rear_mirror_auto_dimming':{'name': u'内后视镜自动防眩目', 'field': 'inside_rear_mirror_auto_dimming'}, # 已删除
    'outside_rear_mirror_auto_dimming':{'name': u'外后视镜自动防眩目', 'field': 'outside_rear_mirror_auto_dimming'}, # 已删除
    'inside_outside_rear_mirror_auto_dimming':{'name': u'内/外后视镜自动防眩目', 'field': 'inside_outside_rear_mirror_auto_dimming'},
    'rear_mirror_power_fold':{'name': u'后视镜电动折叠', 'field': 'rear_mirror_power_fold'},
    'rear_mirror_memory':{'name': u'后视镜记忆', 'field': 'rear_mirror_memory'},
    'rear_window_sunshade':{'name': u'后风挡遮阳帘', 'field': 'rear_window_sunshade'},
    'rear_side_sunshade':{'name': u'后排侧遮阳帘', 'field': 'rear_side_sunshade'},
    'rear_side_privacy_glass':{'name': u'后排侧隐私玻璃', 'field': 'rear_side_privacy_glass'}, # 已删除
    'make_up_mirror':{'name': u'遮阳板化妆镜', 'field': 'make_up_mirror'},
    'rear_wiper':{'name': u'后雨刷', 'field': 'rear_wiper'},
    'sensing_wiper':{'name': u'感应雨刷', 'field': 'sensing_wiper'},
    'manual_air_condition':{'name': u'手动空调', 'field': 'manual_air_condition'}, # 已删除
    'automatic_air_condition':{'name': u'自动空调', 'field': 'automatic_air_condition'}, # 已删除
    'air_condition':{'name': u'空调控制方式', 'field': 'air_condition'},
    'rear_independent_air_condition':{'name': u'后排独立空调', 'field': 'rear_independent_air_condition'},
    'back_seat_outlet':{'name': u'后座出风口', 'field': 'back_seat_outlet'},
    'temperature_zone_control':{'name': u'温度分区控制', 'field': 'temperature_zone_control'},
    'car_air_condition':{'name': u'车内空气调节/花粉过滤', 'field': 'car_air_condition'},
    'car_refrigerator':{'name': u'车载冰箱', 'field': 'car_refrigerator'},
    'automatic_parking_into_place':{'name':u'自动泊车入位', 'field':'automatic_parking_into_place'},
    'engine_start_stop_technology':{'name':u'发动机启停技术', 'field': 'engine_start_stop_technology'},
    'and_line_auxiliary':{'name': u'并线辅助', 'field': 'and_line_auxiliary'},
    'lane_departure_warning_system':{'name': u'车道偏离预警系统', 'field': 'lane_departure_warning_system'},
    'active_brake':{'name': u'主动刹车/主动安全系统', 'field': 'active_brake'},
    'entegral_active_steer':{'name': u'整体主动转向系统', 'field': 'entegral_active_steer'},
    'night_vision_systems':{'name': u'夜视系统', 'field': 'night_vision_systems'},
    'split_screen_display':{'name': u'中控液晶屏分屏显示', 'field': 'split_screen_display'},
    'adaptive_cruise':{'name': u'自适应巡航', 'field': 'adaptive_cruise'},
    'panoramic_camera':{'name': u'全景摄像头', 'field': 'panoramic_camera'},
}