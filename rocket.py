import numpy as np
from numpy import sin, cos, arcsin, pi
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
from scipy.interpolate importinterpld
from mpl_toolkits.basemap import Basemap
import quaternion as qt
import enviroment as env
import coordconv as cc


#Rocketの諸元設定
rocket_settings = {
    'm0': 45247.4,                          #[kg]       初期質量
    'Isp': 266,                             #[s]        SpecificImpulse
    'g0': 9.80665,                          #[m/s^2]    重力定数
    'FT': 1147000,                          #[N]        推力(一定)
    'Tend': 53,                             #[s]        ロケット燃焼終了時間
    'Area': 1.41**2 / 4 * pi,               #[m^2]      基準面積
    'CLa': 3.5,                             #[m^2]      揚力傾斜
    'length_GCM': [-9.76, 0, 0],            #[m]        R/Mジンバル・レバーアーム長
    'length_A': [-1.0, 0, 0],               #[m]        機体空力中心・レバーアーム長
    'Ijj': [188106.0, 188106.0, 1839.0],    #[kg*m^2]   慣性能率
    'IXXdot': 0,                            #[kg*m^2/s] 慣性能率変化率　X軸
    'IYYdot': 0,                            #[kg*m^2/s] 慣性能率変化率　Y軸
    'IZZdot': 0,                            #[kg*m^2/s] 慣性能率変化率　Z軸
    'roll': 0,                              #[deg]      初期ロール
    'pitch': 85.0,                          #[deg]      初期ピッチ角
    'yaw': 120.0,                           #[deg]      初期方位角
    'lat0': 31.251008,                      #[deg]      発射地点緯度 (WGS84)
    'lon0': 131.082301,                     #[deg]      発射地点経度 (WGS84)
    'alt0': 194,                            #[m]        発射地点高度 (WGS84楕円体高)
    #CD定義用のMach数とCDのテーブル
    'match_tbl': np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.4, 1.6,
                           1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]),
    'CD_tbl': np.array([0.28, 0.28, 0.28, 0.29, 0.35, 0.64, 0.67, 0.69,
                        0.66, 0.62, 0.58, 0.55, 0.48, 0.42, 0.38, 0.355,
                        0.33])
}