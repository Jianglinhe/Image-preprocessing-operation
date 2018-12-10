import json
import os
import os.path as osp
import warnings
import PIL.Image
import yaml
from labelme import utils

'''
    @author:hezhiqiang
    function:change json to png with batches
'''

def main():
    # 需要转化json文件所在的文件夹
    json_file = 'C:/Users/visitor/Desktop/data_json/json_file/'

    list = os.listdir(json_file)
    for i in range(0, len(list)):
        path = os.path.join(json_file, list[i])
        if os.path.isfile(path):
            data = json.load(open(path))
            img = utils.img_b64_to_arr(data['imageData'])
            lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])
            captions = ['%d: %s' % (l, name) for l, name in enumerate(lbl_names)]
            lbl_viz = utils.draw_label(lbl, img, captions)
            out_dir = osp.basename(list[i]).replace('.', '_')
            out_dir = osp.join(osp.dirname(list[i]), out_dir)
            if not osp.exists(out_dir):
                os.mkdir(out_dir)

            PIL.Image.fromarray(img).save(osp.join(out_dir, 'img.png'))
            utils.lblsave(osp.join(out_dir, 'label.png'), lbl)
            PIL.Image.fromarray(lbl_viz).save(osp.join(out_dir, 'label_viz.png'))
            with open(osp.join(out_dir, 'label_names.txt'), 'w') as f:
                for lbl_name in lbl_names:
                    f.write(lbl_name + '\n')
            warnings.warn('info.yaml is being replaced by label_names.txt')
            info = dict(label_names=lbl_names)
            with open(osp.join(out_dir, 'info.yaml'), 'w') as f:
                yaml.safe_dump(info, f, default_flow_style=False)
            print('Saved to: %s' % out_dir)


if __name__ == '__main__':
    main()
    main()