"""
Android适配
"""
# config
import os

# 设计宽度 dp
base_smallest_width = 360

# 保存结果的路径
save_fold_path = "dimens/"
# 手机
smallest_width = [320, 360, 384, 392, 400, 410, 411, 432, 480]
# 平板 TV
extra_smallest_width = [533, 592, 600, 640, 662, 720, 768, 800, 811, 820, 960, 961, 1024, 1280, 1365]
# 是否生成 平板 tv的extra_smallest_width dimens.xml 文件?
need_extra_sw = False

# 额外的dp， 默认只转换 1-360 dp
extra_dp = [365, 370, 400, 410, 422, 500, 600, 640, 720]
# 额外的sp   默认只转换 1-40 sp
extra_sp = []


def create_xml_content(base_width, width):
    global extra_dp
    factor = width / base_width
    contents = ["<resources>"]

    dp_list = [x for x in range(1, 361)]
    dp_list.extend(extra_dp)
    for dp in dp_list:
        contents.append("""<dimens name="dp_{0}">{1:.4f}dp</dimens>""".format(dp, dp * factor))

    contents.append("""<!--dp end-->""")
    sp_list = [x for x in range(1, 41)]

    sp_list.extend(extra_sp)

    for sp in sp_list:
        contents.append("""<dimens name="sp_{0}">{1:.4f}sp</dimens>""".format(sp, sp * factor))

    contents.append("</resources>")
    return "\n".join(contents)


def save(width, content):
    global save_fold_path
    folder = save_fold_path + "values-sw{0}dp".format(width)
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(folder + "/dimens.xml", "w+") as f:
        f.write(content)
        f.flush()


def main():
    global smallest_width
    global need_extra_sw
    global base_smallest_width

    if need_extra_sw:
        smallest_width.append(extra_smallest_width)

    for sw in smallest_width:
        save(sw, create_xml_content(base_smallest_width, sw))


if __name__ == '__main__':
    print("begin--------------")
    main()
