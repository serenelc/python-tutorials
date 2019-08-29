from io import BytesIO
import requests
import cv2
import matplotlib.pyplot as plt


def box_intersection(a, b):
    (ax1, ay1, ax2, ay2) = a
    (bx1, by1, bx2, by2) = b
    x1 = max(min(ax1, ax2), min(bx1, bx2))
    y1 = max(min(ay1, ay2), min(by1, by2))
    x2 = min(max(ax1, ax2), max(bx1, bx2))
    y2 = min(max(ay1, ay2), max(by1, by2))
    if x1 < x2 and y1 < y2:
        return (x1, y1, x2, y2)


def box_area(box):
    if box:
        (x1, y1, x2, y2) = box
        return (x2 - x1) * (y2 - y1)
    else:
        return 0


def total_features_area(features):
    area = 0
    for f in features:
        area += box_area(f['bbox'])
    return area


def feature_overlap(crops, features):
    overlap = []
    for crop in crops:
        crop_details = crop['crop']
        x1 = crop_details['x']
        y1 = crop_details['y']
        x2 = crop_details['width'] + x1
        y2 = crop_details['height'] + y1
        bbox = (x1, y1, x2, y2)
        ratio = crop['aspect_ratio']
        total_overlap = 0
        for f in features:
            intersection = box_intersection(bbox, f['bbox'])
            intersecting_area = box_area(intersection)
            total_overlap += intersecting_area
        overlap.append((ratio, total_overlap))
    return overlap


def calc_overlap_percentage(overlap_list, total_feature_area):
    return [(a, round(b / total_feature_area, 3)) for (a, b) in overlap_list]


def draw(crops, features, img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for crop in crops:
        crop_details = crop['crop']
        x1 = crop_details['x']
        y1 = crop_details['y']
        x2 = crop_details['width'] + x1
        y2 = crop_details['height'] + y1
        cropped = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 5)
        for feature in features:
            (xx1, yy1, xx2, yy2) = feature['bbox']
            cropped = cv2.rectangle(cropped, (xx1, yy1), (xx2, yy2), (0, 255, 0), 3)
        plt.imshow(cropped)
        if plt.waitforbuttonpress(0) & 0xFF == 27:
            plt.close()


def crop_image(image_handler, URL = "http://127.0.0.1:5000/api"):
    data = {'settings': '{}'}
    with open(image_handler, "rb") as f:
        print("crop image")
        f = f.read()
        files = {"file": ("image.png", BytesIO(f), f'image/png')}
        print("got file")
        resp = requests.post(URL, data=data, files=files)
        print("made request")
        print(resp.status_code)
        json = resp.json()
        features = json["features"]
        total_feature_area = total_features_area(features)
        crops = json["crops"]
        print(crops)
        print(features)
        overlap_list = feature_overlap(crops, features)
        overlap_percentage = calc_overlap_percentage(overlap_list, total_feature_area)
        print(overlap_percentage)
        img = cv2.imread(image_handler)
        draw(crops, features, img)


if __name__ == '__main__':
    crop_image("Images/group-of-people.jpg")
