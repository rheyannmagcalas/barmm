import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static


barmm_hospitals = {
    'ACCUSAFE DIAGNOSTIC LABORATORY': (6.112780, 125.171670),
    'AMAI PAKPAK MEDICAL CENTER':(8.001110, 124.284820),
    'BALINDONG MUNICIPAL HOSPITAL': (7.912020, 124.198662),
    'BULUAN DISTRICT HOSPITAL': (6.723020, 124.842510),
    'CAMP SIONGCO STATION HOSPITAL': (7.1751214, 124.1889844),
    'COTABATO SANITARIUM': (7.2359082, 124.2669569),
    'DATU ALAWADDIN BANDON SR. MEMORIAL HOSPITAL': (4.8402386, 119.4568401),
    'DATU BLAH T. SINSUAT DISTRICT HOSPITAL': (7.0251188, 124.1604458),
    'DAVAO SPECIALIST CLINIC AND DIAGNOSTIC LABORATORY, INCORPORATED': (7.2242249,124.2437787),
    'DINAIG MUNICIPAL HOSPITAL': (7.0241556, 124.3095705),
    'DR. ABDULLAH HOSPITAL FOUNDATION INC': (8.0118259, 124.2765455),
    'DR. JOSE MA. TORRES MEMORIAL FOUNDATION HOSPITAL INC.': (6.6468373, 122.0995113),
    'DR. SERAPIO B. MONTAÑER JR. AL-HAJ MEMORIAL HOSPITAL': (7.5808064, 124.0789301),
    'EDIBORAH P.  YAP MEMORIAL HOSPITAL': (6.6529057, 122.1333005),
    'MAGUINDANAO PROVINCIAL HOSPITAL': (6.8511263, 124.4281933),
    'MINDALANO SPECIALIST HOSPITAL FOUNDATION LABORATORY': (8.0010603, 124.2979363),
    'PARANG DISTRICT HOSPITAL': (5.9182933, 120.9138393),
    'RALPH EDMUND SPENCER FOUNDATION INC. HOSPITAL': (7.6275856, 124.0701798),
    'SIASI DISTRICT HOSPITAL': (5.5419017, 120.8157036),
    'SOUTH UPI MUNICIPAL HOSPITAL': (6.8568678, 124.1445611),
    'SULU PROVINCIAL HOSPITAL': (6.0466158, 120.9994215),
    'SULU SANITARIUM': (6.0503503,121.0038253),
    'TAMPARAN DISTRICT HOSPITAL': (7.8783217, 124.3295037),
    'TAMPARAN MEDICAL FOUNDATION INC. HOSPITAL': (7.876438, 124.3257791),
    'TAPUL MUNICIPAL HOSPITAL': (5.717606,120.8835988),
    'COTABATO REGIONAL AND MEDICAL CENTER': (7.2002412, 124.2341011)
}


barmm_hospitals_details = {
    'ACCUSAFE DIAGNOSTIC LABORATORY': {
        'latitude': 6.112780,
        'longtitude': 125.171670,
        'city': 'Cotabato City',
        'address': '457C+52 General Santos City, South Cotabato'
        #6.1129044,125.1678318
    },
    'AMAI PAKPAK MEDICAL CENTER':{
        'latitude': 8.001110,
        'longtitude': 124.284820,
        'city': 'Lanao del Sur',
        'address': '273M+RH Marawi City, Lanao del Sur'
        
        #8.0045342,124.2818008
    },
    'BALINDONG MUNICIPAL HOSPITAL': {
        'latitude': 7.912020,
        'longtitude': 124.198662,
        'city': 'Lanao del Sur',
        'address': 'W682+Q2 Balindong, Lanao del Sur'
        
        #7.9169693,124.1979043
    },
    'BULUAN DISTRICT HOSPITAL': {
        'latitude': 6.723020,
        'longtitude': 124.842510,
        'city': 'Maguindanao',
        'address': 'PQFX+63 Mangudadatu, Maguindanao'
        
        #6.7230837,124.7955522
    },
    'CAMP SIONGCO STATION HOSPITAL': {
        'latitude': 7.1751214,
        'longtitude': 124.1889844,
        'city': 'Maguindanao',
        'address': '55QM+GJ Datu Odin Sinsuat, Maguindanao'
        #7.1751214,124.1889844
    },
    'COTABATO SANITARIUM': {
        'latitude': 7.2359082,
        'longtitude': 124.2669569,
        'city': 'Maguindanao',
        'address': '67P9+9M Sultan Kudarat, Maguindanao'
        #7.2359082,124.2669569
    },
    'DATU ALAWADDIN BANDON SR. MEMORIAL HOSPITAL': {
        'latitude': 4.8402386,
        'longtitude': 119.4568401,
        'city': 'Tawi-Tawi',
        'address': 'RFR5+3J Sibutu, Tawi-Tawi'
        #4.8402386,119.4568401
    },
    'DATU BLAH T. SINSUAT DISTRICT HOSPITAL': {
        'latitude': 7.0251188,
        'longtitude': 124.1604458,
        'city': 'Maguindanao',
        'address': '25J7+4V Upi, Maguindanao'
        #7.0251188,124.1604458
    },
    'DAVAO SPECIALIST CLINIC AND DIAGNOSTIC LABORATORY, INCORPORATED': {
        'latitude': 7.2242249,
        'longtitude': 124.2437787,
        'city': 'Maguindanao',
        'address': '66FW+M9 Cotabato City, Maguindanao'
        #7.2242249,124.2437787
    },
    'DINAIG MUNICIPAL HOSPITAL': {
        'latitude': 7.0241556,
        'longtitude': 124.3095705,
        'city': 'Maguindanao',
        'address': '28F6+MP Datu Odin Sinsuat, Maguindanao'
        #7.0241556,124.3095705
    },
    'DR. ABDULLAH HOSPITAL FOUNDATION INC': {
        'latitude': 8.0118259,
        'longtitude': 124.2765455,
        'city': 'Lanao del Sur',
        'address': '276H+PF Marawi City, Lanao del Sur'
        #8.0118259,124.2765455
    },
    'DR. JOSE MA. TORRES MEMORIAL FOUNDATION HOSPITAL INC.': {
        'latitude': 6.6468373,
        'longtitude': 122.0995113,
        'city': 'Basilan',
        'address': 'J4W2+PM Lamitan City, Basilan'
        #6.6468373,122.0995113
    },
    'DR. SERAPIO B. MONTAÑER JR. AL-HAJ MEMORIAL HOSPITAL': {
        'latitude': 7.5808064,
        'longtitude': 124.0789301,
        'city': 'Lanao del Sur',
        'address': 'H3JJ+8C Malabang, Lanao del Sur'
        #7.5808064,124.0789301
    },
    'EDIBORAH P.  YAP MEMORIAL HOSPITAL': {
        'latitude': 6.6529057,
        'longtitude': 122.1333005,
        'city': 'Basilan',
        'address': 'M43P+55 Lamitan City, Basilan'
        #6.6529057,122.1333005
    },
    'MAGUINDANAO PROVINCIAL HOSPITAL': {
        'latitude': 6.8511263,
        'longtitude': 124.4281933,
        'city': 'Maguindanao',
        'address': 'VC2J+C5 Shariff Aguak, Maguindanao'
        #6.8511263,124.4281933
    },
    'MINDALANO SPECIALIST HOSPITAL FOUNDATION LABORATORY': {
        'latitude': 8.0010603,
        'longtitude': 124.2979363,
        'city': 'Lanao del Sur',
        'address': '2822+C2 Marawi City, Lanao del Sur'
        #8.0010603,124.2979363
    },
    'PARANG DISTRICT HOSPITAL': {
        'latitude': 5.9182933,
        'longtitude': 120.9138393,
        'city': 'Sulu',
        'address': 'WW98+8C Parang, Sulu'
        #5.9182933,120.9138393
    },
    'RALPH EDMUND SPENCER FOUNDATION INC. HOSPITAL': {
        'latitude': 7.6275856,
        'longtitude': 124.0701798,
        'city': 'Lanao del Sur',
        'address': 'J3HC+2W Malabang, Lanao del Sur'
        #7.6275856,124.0701798
    },
    'SIASI DISTRICT HOSPITAL': {
        'latitude': 5.5419017,
        'longtitude': 120.8157036,
        'city': 'Sulu',
        'address': 'Sulu'
        #5.5419017,120.8157036
    },
    'SOUTH UPI MUNICIPAL HOSPITAL': {
        'latitude': 6.8568678,
        'longtitude': 124.1445611,
        'city': 'Maguindanao',
        'address': 'V45W+GX South Upi, Maguindanao'
        #6.8568678,124.1445611
    },
    'SULU PROVINCIAL HOSPITAL': {
        'latitude': 6.0466158,
        'longtitude': 120.9994215,
        'city': 'Sulu',
        'address': '22W2+JJ Jolo, Sulu'
        #6.0466158,120.9994215
    },
    'SULU SANITARIUM': {
        'latitude': 6.0503503,
        'longtitude': 121.0038253,
        'city': 'Sulu',
        'address': '3224+4C Jolo, Sulu'
        #6.0503503,121.0038253
    },
    'TAMPARAN DISTRICT HOSPITAL': {
        'latitude': 7.8783217,
        'longtitude': 124.3295037,
        'city': 'Lanao del Sur',
        'address': 'V8JM+25 Tamparan, Lanao del Sur'
        #7.8783217,124.3295037
    },
    'TAMPARAN MEDICAL FOUNDATION INC. HOSPITAL': {
        'latitude': 7.876438,
        'longtitude': 124.3257791,
        'city': 'Lanao del Sur',
        'address': 'V8GH+H5 Tamparan, Lanao del Sur'
        #7.876438,124.3257791
    },
    'TAPUL MUNICIPAL HOSPITAL': {
        'latitude': 5.717606,
        'longtitude': 120.8835988,
        'city': 'Sulu',
        'address': 'PWJ3+53 Tapul, Sulu'
        #5.717606,120.8835988
    },
    'COTABATO REGIONAL AND MEDICAL CENTER': {
        'latitude': 7.2002412,
        'longtitude': 124.2341011,
        'city': 'Maguindanao',
        'address': '662P+3G Cotabato City, Maguindanao'
        #7.2002412,124.2341011
    }
}

import math

def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))


genre = st.sidebar.radio(
    " ",
    ('Hospitals', 'Proposal'))


option = st.selectbox(
        'Hospitals', ('All', 'Search'))

if option == 'Search':
    current_location = st.selectbox(
            'Current Hospital Location', ['ACCUSAFE DIAGNOSTIC LABORATORY', 'AMAI PAKPAK MEDICAL CENTER', 'BALINDONG MUNICIPAL HOSPITAL', 'BULUAN DISTRICT HOSPITAL', 'CAMP SIONGCO STATION HOSPITAL', 'COTABATO SANITARIUM', 'DATU ALAWADDIN BANDON SR. MEMORIAL HOSPITAL', 'DATU BLAH T. SINSUAT DISTRICT HOSPITAL', 'DAVAO SPECIALIST CLINIC AND DIAGNOSTIC LABORATORY, INCORPORATED', 'DINAIG MUNICIPAL HOSPITAL', 'DR. ABDULLAH HOSPITAL FOUNDATION INC', 'DR. JOSE MA. TORRES MEMORIAL FOUNDATION HOSPITAL INC.', 'DR. SERAPIO B. MONTAÑER JR. AL-HAJ MEMORIAL HOSPITAL', 'EDIBORAH P.  YAP MEMORIAL HOSPITAL', 'MAGUINDANAO PROVINCIAL HOSPITAL', 'MINDALANO SPECIALIST HOSPITAL FOUNDATION LABORATORY', 'PARANG DISTRICT HOSPITAL', 'RALPH EDMUND SPENCER FOUNDATION INC. HOSPITAL', 'SIASI DISTRICT HOSPITAL', 'SOUTH UPI MUNICIPAL HOSPITAL', 'SULU PROVINCIAL HOSPITAL', 'SULU SANITARIUM', 'TAMPARAN DISTRICT HOSPITAL', 'TAMPARAN MEDICAL FOUNDATION INC. HOSPITAL', 'TAPUL MUNICIPAL HOSPITAL', 'COTABATO REGIONAL AND MEDICAL CENTER'])
    
    if st.button('Search'):
        st.subheader('Top 10 Nearest Hospital')
        search_result = dict()
        
        for hospital in barmm_hospitals.keys():
            if current_location != hospital:
                distance = haversine(barmm_hospitals[current_location], barmm_hospitals[hospital])
                
                search_result[distance] = hospital
        
        search_keys = list(search_result.keys())
        
        m = folium.Map(location = [barmm_hospitals[current_location][0],barmm_hospitals[current_location][1]],
                       zoom_start=7, 
                       control_scale=True,
                       prefer_canvas=True)
        
        nearest_hospitals = []
        nearest_address = []
        nearest_province = []
        
        counter = 0
        
        folium.Marker(
                    [barmm_hospitals[current_location][0], barmm_hospitals[current_location][1]], popup=barmm_hospitals[current_location], 
            icon=folium.Icon(color='red',icon="hospital-o", prefix='fa'),
            tooltip=current_location
        ).add_to(m)
        
        for _search in sorted(search_keys)[0:10]:       
            counter +=1
            if counter == 1 or counter == 2 or counter == 3:
                folium.Marker(
                    [barmm_hospitals[search_result[_search]][0], barmm_hospitals[search_result[_search]][1]], popup=search_result[_search], 
                    icon=folium.Icon(color='green',icon="hospital-o", prefix='fa'),
                    tooltip=search_result[_search]
                ).add_to(m)
            else:
                folium.Marker(
                    [barmm_hospitals[search_result[_search]][0], barmm_hospitals[search_result[_search]][1]], popup=search_result[_search], tooltip=search_result[_search]
                ).add_to(m)
            
            nearest_hospitals.append(search_result[_search])
            nearest_province.append(barmm_hospitals_details[search_result[_search]]['city'])
            nearest_address.append(barmm_hospitals_details[search_result[_search]]['address'])
            
        folium_static(m)
        
        df_hospitals = {
            'Hospitals': nearest_hospitals,
            'Province': nearest_province,
            'Address': nearest_address
        }
        
        df_hospitals = pd.DataFrame(data=df_hospitals)
        df_hospitals = df_hospitals.set_index(['Hospitals'])
        st.table(df_hospitals)
        
else:
    st.subheader('BARMM Hospitals')
    m = folium.Map(location = [7.6955724,122.0074178],
                       zoom_start=7, 
                       control_scale=True,
                       prefer_canvas=True)

    folium.Marker(
        [8.001110, 125.171670], popup="ACCUSAFE DIAGNOSTIC LABORATORY", tooltip='ACCUSAFE DIAGNOSTIC LABORATORY'
    ).add_to(m)

    folium.Marker(
        [8.001110, 124.284820], popup="AMAI PAKPAK MEDICAL CENTER", tooltip='AMAI PAKPAK MEDICAL CENTER'
    ).add_to(m)

    folium.Marker(
        [7.912020, 124.198662], popup="BALINDONG MUNICIPAL HOSPITAL", tooltip='BALINDONG MUNICIPAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [6.723020, 124.842510], popup="BULUAN DISTRICT HOSPITAL", tooltip='BULUAN DISTRICT HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.1751214, 124.1889844], popup="CAMP SIONGCO STATION HOSPITAL", tooltip='CAMP SIONGCO STATION HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.2359082, 124.2669569], popup="COTABATO SANITARIUM", tooltip='COTABATO SANITARIUM'
    ).add_to(m)

    folium.Marker(
        [4.8402386, 119.4568401], popup="DATU ALAWADDIN BANDON SR. MEMORIAL HOSPITAL", tooltip='DATU ALAWADDIN BANDON SR. MEMORIAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.0251188, 124.1604458], popup="DATU BLAH T. SINSUAT DISTRICT HOSPITAL", tooltip='DATU BLAH T. SINSUAT DISTRICT HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.2242249, 124.2437787], popup="DAVAO SPECIALIST CLINIC AND DIAGNOSTIC LABORATORY, INCORPORATED", tooltip='DAVAO SPECIALIST CLINIC AND DIAGNOSTIC LABORATORY, INCORPORATED'
    ).add_to(m)

    folium.Marker(
        [7.0241556, 124.3095705], popup="DINAIG MUNICIPAL HOSPITAL", tooltip='DINAIG MUNICIPAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [8.0118259, 124.2765455], popup="DR. ABDULLAH HOSPITAL FOUNDATION INC", tooltip='DR. ABDULLAH HOSPITAL FOUNDATION INC'
    ).add_to(m)

    folium.Marker(
        [6.6468373, 122.0995113], popup="DR. JOSE MA. TORRES MEMORIAL FOUNDATION HOSPITAL INC.", tooltip='DR. JOSE MA. TORRES MEMORIAL FOUNDATION HOSPITAL INC.'
    ).add_to(m)

    folium.Marker(
        [7.5808064, 124.0789301], popup="DR. SERAPIO B. MONTAÑER JR. AL-HAJ MEMORIAL HOSPITAL", tooltip='DR. SERAPIO B. MONTAÑER JR. AL-HAJ MEMORIAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [6.6529057, 122.1333005], popup="EDIBORAH P. YAP MEMORIAL HOSPITAL", tooltip='EDIBORAH P. YAP MEMORIAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [6.8511263, 124.4281933], popup="MAGUINDANAO PROVINCIAL HOSPITAL", tooltip='MAGUINDANAO PROVINCIAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [8.0010603, 124.2979363], popup="MINDALANO SPECIALIST HOSPITAL FOUNDATION LABORATORY", tooltip='MINDALANO SPECIALIST HOSPITAL FOUNDATION LABORATORY'
    ).add_to(m)

    folium.Marker(
        [5.9182933, 120.9138393], popup="PARANG DISTRICT HOSPITAL", tooltip='PARANG DISTRICT HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.6275856, 124.0701798], popup="RALPH EDMUND SPENCER FOUNDATION INC. HOSPITAL", tooltip='RALPH EDMUND SPENCER FOUNDATION INC. HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [5.5419017, 120.8157036], popup="SIASI DISTRICT HOSPITAL", tooltip='SIASI DISTRICT HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [6.8568678, 124.1445611], popup="SOUTH UPI MUNICIPAL HOSPITAL", tooltip='SOUTH UPI MUNICIPAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [6.0466158, 120.9994215], popup="SULU PROVINCIAL HOSPITAL", tooltip='SULU PROVINCIAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [6.0503503, 121.0038253], popup="SULU SANITARIUM", tooltip='SULU SANITARIUM'
    ).add_to(m)

    folium.Marker(
        [7.8783217, 124.3295037], popup="TAMPARAN DISTRICT HOSPITAL", tooltip='TAMPARAN DISTRICT HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.876438, 124.3257791], popup="TAMPARAN MEDICAL FOUNDATION INC. HOSPITAL", tooltip='TAMPARAN MEDICAL FOUNDATION INC. HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [5.717606, 120.8835988], popup="TAPUL MUNICIPAL HOSPITAL", tooltip='TAPUL MUNICIPAL HOSPITAL'
    ).add_to(m)

    folium.Marker(
        [7.2002412, 124.2341011], popup="COTABATO REGIONAL AND MEDICAL CENTER", tooltip='TAPUL MUNICIPAL HOSPITAL'
    ).add_to(m)

    folium_static(m)

        
    df_hospitals = {
        'Hospitals': ['ACCUSAFE DIAGNOSTIC LABORATORY', 'AMAI PAKPAK MEDICAL CENTER', 'BALINDONG MUNICIPAL HOSPITAL', 'BULUAN DISTRICT HOSPITAL', 'CAMP SIONGCO STATION HOSPITAL', 'COTABATO SANITARIUM', 'DATU ALAWADDIN BANDON SR. MEMORIAL HOSPITAL', 'DATU BLAH T. SINSUAT DISTRICT HOSPITAL', 'DAVAO SPECIALIST CLINIC AND DIAGNOSTIC LABORATORY, INCORPORATED', 'DINAIG MUNICIPAL HOSPITAL', 'DR. ABDULLAH HOSPITAL FOUNDATION INC', 'DR. JOSE MA. TORRES MEMORIAL FOUNDATION HOSPITAL INC.', 'DR. SERAPIO B. MONTAÑER JR. AL-HAJ MEMORIAL HOSPITAL', 'EDIBORAH P.  YAP MEMORIAL HOSPITAL', 'MAGUINDANAO PROVINCIAL HOSPITAL'], 
        'Province': ['Cotabato City', 'Lanao del Sur', 'Lanao del Sur', 'Maguindanao', 'Maguindanao',  'Maguindanao', 'Tawi-Tawi', 'Maguindanao', 'Maguindanao', 'Maguindanao', 'Lanao del Sur', 'Basilan', 'Lanao del Sur', 'Basilan', 'Maguindanao'], 
        'Address': ['457C 52 General Santos City, South Cotabato', '273M RH Marawi City, Lanao del Sur', 
                    'W682 Q2 Balindong, Lanao del Sur', 'PQFX 63 Mangudadatu, Maguindanao',
                    '55QM GJ Datu Odin Sinsuat, Maguindanao', '67P9 9M Sultan Kudarat, Maguindanao',
                    'RFR5 3J Sibutu, Tawi-Tawi', '25J7 4V Upi, Maguindanao', 
                    '66FW M9 Cotabato City, Maguindanao', '28F6 MP Datu Odin Sinsuat, Maguindanao',
                    '276H PF Marawi City, Lanao del Sur', 'J4W2 PM Lamitan City, Basilan',
                    'H3JJ 8C Malabang, Lanao del Sur',  'M43P 55 Lamitan City, Basilan', 'VC2J C5 Shariff Aguak, Maguindanao']}

    df_hospitals = pd.DataFrame(data=df_hospitals)
    df_hospitals = df_hospitals.set_index(['Hospitals'])
    st.table(df_hospitals)