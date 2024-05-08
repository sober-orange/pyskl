# 关于PYSKL数据格式，您需要了解的内容

PYSKL现在提供用于训练和测试的预处理 pickle 标注文件。预处理脚本将在以后的更新中发布。下面我们将演示标注文件的格式，并提供下载链接。

## pickle文件的格式

每个pickle文件对应于一个动作识别数据集。pickle文件的内容是一个包含两个字段的字典：split 和 annotations

1. `split`：split 字段的值是一个字典：`key` 是 split 名称，而 value 是属于特定剪辑的视频标识符列表。
2. `annotations`：annotations 字段的值是骨架标注的列表，每个骨架标注都是一个字典，包含以下字段：
	1. `frame_dir` (str)：对应视频的标识。
	2. `total_frames` (int)：此视频中的帧数。
	3. `img_shape` (tuple[int])：视频帧的形状，一个包含两个元素的元组，格式为（height，width）。仅二维骨架需要。
	4. `original_shape` (tuple[int])：与 `img_shape` 相同。
	5. `label` (int)：action 标签。
	6. `keypoint` (np.ndarray，形状为[M x T x V x C])：关键点标注。
		- M：人数；
		- T： 帧数（与 `total_frames` 相同）；
		- V： 关键点的数量（25 个用于 NTURGB+D 3D 骨架，17 个用于 CoCo，18 个用于 OpenPose 等）；
		- C： 关键点坐标的维数（对于2D关键点，C=2，对于3D关键点，C=3）。
	7. `keypoint_score` (np.ndarray，形状[M x T x V])：关键点的置信度得分。仅二维骨架需要。




Note:
1. 对于Kinetics400，情况有点不同（对于存储节省和训练加速）：
	1. 字段 `keypoint`、`keypoint_score` 不在标注文件中，而是存储在许多不同的kpfile中。
	2. 一个名为 `raw_file` 的新字段，用于指定包含此视频的骨架注释的 kpfile 的文件路径。
	3. 每个 kpfile 都是一个字典：key 是 frame_dir，value 是一个带有单个关键点的字典。关键点的值是形状为[N x V x C]的ndarray。N： 视频中骨架的数量；V： 关键点的数量；C（C=3）：关键点（x，y，分数）的维数。
	4. 一个名为 `frame_inds` 的新字段指示每个骨架的相应帧索引。
	5. 一个名为 `box_score` 的新字段指示每个骨架的相应 bbox 分数。
	6. 一个名为 `valid` 的新字段指示当我们只保留bbox分数大于阈值的骨架时，还剩多少帧（具有有效骨架）。
	7. 我们使用 memcache 将 kpfile 缓存在内存中，并使用 frame_dir 进行查询以获得骨架标注。Kinetics-400 骨架使用 DecompressPose 操作转换为正常骨骼格式。

您可以下载一个标注文件并浏览它以熟悉我们的标注格式。

## 下载预处理的骨架

我们提供了预处理骨架标注的链接，您可以直接下载它们并将其用于训练和测试。

- NTURGB+D [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_hrnet.pkl)
- NTURGB+D [3D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_3danno.pkl](https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu60_3danno.pkl)
- NTURGB+D 120 [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu120_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu120_hrnet.pkl)
- NTURGB+D 120 [3D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu120_3danno.pkl](https://download.openmmlab.com/mmaction/pyskl/data/nturgbd/ntu120_3danno.pkl)
- GYM [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/gym/gym_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/gym/gym_hrnet.pkl)
    - GYM 2D skeletons are extracted with ground-truth human bounding boxes, which can be downloaded with link: [https://download.openmmlab.com/mmaction/pyskl/data/gym/gym_gt_bboxes.pkl](https://download.openmmlab.com/mmaction/pyskl/data/gym/gym_gt_bboxes.pkl). Please cite [PoseConv3D](https://arxiv.org/abs/2104.13586) if you use it in your project.
- UCF101 [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/ucf101/ucf101_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/ucf101/ucf101_hrnet.pkl)
- HMDB51 [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/hmdb51/hmdb51_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/hmdb51/hmdb51_hrnet.pkl)
- Diving48 [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/diving48/diving48_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/diving48/diving48_hrnet.pkl)
- Kinetics400 [2D Skeleton]: [https://download.openmmlab.com/mmaction/pyskl/data/k400/k400_hrnet.pkl](https://download.openmmlab.com/mmaction/pyskl/data/k400/k400_hrnet.pkl) (Table of contents only, no skeleton annotations)

对于 Kinetics400，由于骨架标注较大，我们不提供阿里云上的直接下载链接。请使用以下链接下载 kpfiles 并提取到 $PYSKL/data/k400 文件夹下，用于 Kinetics-400 训练和测试：[https://mycuhk-my.sharepoint.com/:u:/g/personal/1155136485_link_cuhk_edu_hk/EeyDCVskqLtClMVVwqD53acBF2FEwkctp3vtRbkLfnKSTw?e=B3SZlM](https://mycuhk-my.sharepoint.com/:u:/g/personal/1155136485_link_cuhk_edu_hk/EeyDCVskqLtClMVVwqD53acBF2FEwkctp3vtRbkLfnKSTw?e=B3SZlM)




## 处理 NTURGB+D 原始骨架文件

0. 假设您使用当前目录作为工作目录，即 $PYSKL/tools/data
1. 从 NTURGB+D 的官方存储库下载原始骨架文件，解压缩所有 `.skeleton` 文件并将其放在一个文件夹中（在我的示例中命名为 `nturgb+d_skeletons`）。
2. 运行 `python ntu_preproc.py` 生成已处理的骨架标注，它将在当前工作目录下生成 `ntu60_3danno.pkl` 和 `ntu120_3danno.pkl`（如果您也下载了 NTURGB+D 120 骨架）。

PS：为了获得最佳的预处理速度，请将 ntu_preproc.py 中的 num_process 更改为CPU的核数。



























