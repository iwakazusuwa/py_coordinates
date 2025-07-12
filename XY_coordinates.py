import cv2
import subprocess

#=============================================
# 画像名指定　1380×840
#=============================================
in_a = "aa.png"

#---ポチポチ数（画像の形によって変更します
kazu = 16


#=============================================
# ポインタ等の細かい指定とか
#=============================================
def onMouse(event, x, y, flag, params):
    raw_img = params["img"]
    wname = params["wname"]
    point_list = params["point_list"]
    point_num = params["point_num"]
    
    # 左クリックでポイント追加
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(point_list) < point_num:
            point_list.append([x, y])
              
    # 右クリックでポイント削除
    if event == cv2.EVENT_RBUTTONDOWN:
        if len(point_list) > 0:
            point_list.pop(-1)
    
    # 画像描画
    img = raw_img.copy()
    h, w = img.shape[0], img.shape[1]
    cv2.line(img, (x, 0), (x, h), (255, 0, 0), 1)
    cv2.line(img, (0, y), (w, y), (255, 0, 0), 1)

    # 点と線の描画
    for i in range(len(point_list)):
        cv2.circle(img, (point_list[i][0], point_list[i][1]), 3, (0, 0, 255), 3)
        if i > 0:
            cv2.line(
                img,
                (point_list[i][0], point_list[i][1]),
                (point_list[i - 1][0], point_list[i - 1][1]),
                (0, 255, 0),
                2,
            )
        if i == point_num - 1:
            cv2.line(
                img,
                (point_list[i][0], point_list[i][1]),
                (point_list[0][0], point_list[0][1]),
                (0, 255, 0),
                2,
            )

    if 0 < len(point_list) < point_num:
        cv2.line(
            img,
            (x, y),
            (point_list[-1][0], point_list[-1][1]),
            (0, 255, 0),
            2,
        )

    # 座標表示
    cv2.putText(
        img,
        "({0}, {1})".format(x, y),
        (0, 20),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )

    cv2.imshow(wname, img)

#=============================================
# 取得した情報を保存
#=============================================
def save_point_list(path, point_list):
    with open(path, "w") as f:
        for p in point_list:
            f.write(f"{p[0]},{p[1]}\n")

#=============================================
# 画像の上にポチポチしていく
#============================================
def main():
    # 画像読み込み
    img = cv2.imread(in_a)
    if img is None:
        print("画像が読み込めません。パスを確認してください。")
        return

    wname = "MouseEvent"
    point_list = []
    point_num = kazu

    params = {
        "img": img,
        "wname": wname,
        "point_list": point_list,
        "point_num": point_num,
    }

    cv2.namedWindow(wname)
    cv2.setMouseCallback(wname, onMouse, params)
    cv2.imshow(wname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(point_list) == point_num:
        txt_path ="points.csv"
        save_point_list(txt_path, point_list)
        print("Saved csv file:", txt_path)

if __name__ == "__main__":
    main()

#============================================
# エクセルで開く
#============================================
EXCEL = r"points.csv"
subprocess.Popen(["start", EXCEL], shell=True)

