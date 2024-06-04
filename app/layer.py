# layer.py
import folium

def add_brand_layers(m, brand_areas, polygons, negative_areas):
    # ブランドエリアを青色のポリゴンで表示
    for brand in brand_areas['brand']:
        for polygon in polygons[brand]:  # 各ブランドごとにポリゴンを追加
            folium.Polygon(
                locations=polygon,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.3,
                popup=brand,
                tooltip=folium.Tooltip(brand)
            ).add_to(m)

    # ブランドに対するネガティブな要素を持つエリアを赤色の円で表示
    for brand, areas in negative_areas.items():  # 複数の座標データを処理
        for area in areas:
            folium.Circle(
                location=(area['latitude'], area['longitude']),
                radius=area['radius'],
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.2,
                popup=brand,
                tooltip=folium.Tooltip(brand)
            ).add_to(m)
    
    return m
