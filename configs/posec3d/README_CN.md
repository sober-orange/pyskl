# PoseC3D


## Introduction

PoseC3D 是第一个将 2D 人体骨架格式化为 3D 体素并使用 3D ConvNets 处理人体骨架的框架。我们发布了多个用不同 backbone 实例化并在不同数据集上训练的 PoseC3D 变体。


![](https://user-images.githubusercontent.com/34324155/142995620-21b5536c-8cda-48cd-9cb9-50b70cab7a89.png)

## Citation

```BibTeX
@article{duan2021revisiting,
  title={Revisiting skeleton-based action recognition},
  author={Duan, Haodong and Zhao, Yue and Chen, Kai and Lin, Dahua and Dai, Bo},
  journal={arXiv preprint arXiv:2104.13586},
  year={2021}
}
```

## Model Zoo

我们发布了在各种数据集上使用多个 3D backbone 训练的许多权重。每种形式的 accuracy 链接到权重文件。

|Dataset|Backbone|Annotation|Pretrain|Training Epochs|GPUs|Joint Top-1  <br>Config Link: Weight Link|Limb Top-1  <br>Config Link: Weight Link|Two-Stream Top1|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|NTURGB+D XSub|SlowOnly-R50|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_ntu60_xsub/joint.py): [93.7](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu60_xsub/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_ntu60_xsub/limb.py): [93.4](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu60_xsub/limb.pth)|94.1|
|NTURGB+D XSub|C3D-light|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/c3d_light_ntu60_xsub/joint.py): [92.7](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/c3d_light_ntu60_xsub/joint.pth)|[limb_config](file://configs/posec3d/c3d_light_ntu60_xsub/limb.py): [92.6](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/c3d_light_ntu60_xsub/limb.pth)|93.3|
|NTURGB+D XSub|X3D-Shallow|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/x3d_shallow_ntu60_xsub/joint.py): [92.1](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/x3d_shallow_ntu60_xsub/joint.pth)|[limb_config](file://configs/posec3d/x3d_shallow_ntu60_xsub/limb.py): [91.6](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/x3d_shallow_ntu60_xsub/limb.pth)|92.4|
|NTURGB+D XView|SlowOnly-R50|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_ntu60_xview/joint.py): [96.5](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu60_xview/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_ntu60_xview/limb.py): [96.0](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu60_xview/limb.pth)|96.9|
|NTURGB+D 120 XSub|SlowOnly-R50|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_ntu120_xsub/joint.py): [85.9](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu120_xsub/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_ntu120_xsub/limb.py): [85.9](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu120_xsub/limb.pth)|86.7|
|NTURGB+D 120 XSet|SlowOnly-R50|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_ntu120_xset/joint.py): [89.7](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu120_xset/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_ntu120_xset/limb.py): [89.7](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ntu120_xset/limb.pth)|90.3|
|Kinetics-400|SlowOnly-R50 (stages: 3, 4, 6)|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_346_k400/joint.py): [47.3](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_346_k400/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_346_k400/limb.py): [46.9](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_346_k400/limb.pth)|49.1|
|Kinetics-400|SlowOnly-R50 (stages: 4, 6, 3)|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_463_k400/joint.py): [46.6](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_463_k400/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_463_k400/limb.py): [45.7](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_463_k400/limb.pth)|47.7|
|FineGYM¹|SlowOnly-R50|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_gym/joint.py): [93.8](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_gym/joint.pth)|[limb_config](file://configs/posec3d/slowonly_r50_gym/limb.py): [93.8](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_gym/limb.pth)|94.1|
|FineGYM¹|C3D-light|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/c3d_light_gym/joint.py): [91.8](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/c3d_light_gym/joint.pth)|[limb_config](file://configs/posec3d/c3d_light_gym/limb.py): [91.2](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/c3d_light_gym/limb.pth)|92.1|
|FineGYM¹|X3D-shallow|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/x3d_shallow_gym/joint.py): [91.4](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/x3d_shallow_gym/joint.pth)|[limb_config](file://configs/posec3d/x3d_shallow_gym/limb.py): [90.0](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/x3d_shallow_gym/limb.pth)|91.8|
|UCF101²|SlowOnly-R50|HRNet 2D Pose|Kinetics-400|120|8|[joint_config](file://configs/posec3d/slowonly_r50_ucf101_k400p/s1_joint.py): [86.9](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_ucf101_k400p/s1_joint.pth)|||
|HMDB51²|SlowOnly-R50|HRNet 2D Pose|Kinetics-400|120|8|[joint_config](file://configs/posec3d/slowonly_r50_hmdb51_k400p/s1_joint.py): [69.4](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_hmdb51_k400p/s1_joint.pth)|||
|Diving48|SlowOnly-R50|HRNet 2D Pose|None|240|8|[joint_config](file://configs/posec3d/slowonly_r50_diving48/joint.py): [54.5](http://download.openmmlab.com/mmaction/pyskl/ckpt/posec3d/slowonly_r50_diving48/joint.pth)|||

**Note**

1. 对于 FineGYM，我们报告的是平均类Top-1精度，而不是Top-1精度。
2. 对于 UCF101 和 HMDB51，我们提供在 official split 1 上训练的 checkpoints。
3. 我们使用线性学习率（`Initial LR` ∝ `Batch Size`）。如果你更改了训练的 batch size，请记得按比例更改初始LR。
4. 尽管进行了优化，但多剪辑测试可能会消耗大量时间。为了更快地推断，您可以更改 test_pipeline 以禁用多剪辑测试，这可能会导致识别性能的小幅下降。以下是指南：

   ```python
   test_pipeline = [
       dict(type='UniformSampleFrames', clip_len=48, num_clips=10),	# Change `num_clips=10` to `num_clips=1`
       dict(type='PoseDecode'),
       dict(type='PoseCompact', hw_ratio=1., allow_imgpad=True),
       dict(type='Resize', scale=(64, 64), keep_ratio=False),
       dict(type='GeneratePoseTarget', with_kp=True, with_limb=False, double=True, left_kp=left_kp, right_kp=right_kp),	# Change `double=True` to `double=False`
       dict(type='FormatShape', input_format='NCTHW_Heatmap'),
       dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
       dict(type='ToTensor', keys=['imgs'])
   ]
   ```

## Demonstration of heatmap volumes

|**Pose Estimation Results**  <br>![](https://user-images.githubusercontent.com/34324155/116529341-6fc95080-a90f-11eb-8f0d-57fdb35d1ba4.gif)  <br>  <br>![](https://user-images.githubusercontent.com/34324155/116531676-04cd4900-a912-11eb-8db4-a93343bedd01.gif)|**Keypoint Heatmap Volume Visualization**  <br>![](https://user-images.githubusercontent.com/34324155/116529336-6dff8d00-a90f-11eb-807e-4d9168997655.gif)  <br>  <br>![](https://user-images.githubusercontent.com/34324155/116531658-00a12b80-a912-11eb-957b-561c280a86da.gif)|**Limb Heatmap Volume Visualization**  <br>![](https://user-images.githubusercontent.com/34324155/116529322-6a6c0600-a90f-11eb-81df-6fbb36230bd0.gif)  <br>  <br>![](https://user-images.githubusercontent.com/34324155/116531649-fed76800-a911-11eb-8ca9-0b4e58f43ad9.gif)|
|---|---|---|

## Training & Testing

可以使用以下命令来训练模型。

```shell
bash tools/dist_train.sh ${CONFIG_FILE} ${NUM_GPUS} [optional arguments]
# For example: train PoseC3D on FineGYM (HRNet 2D skeleton, Joint Modality) with 8 GPUs, with validation, and test the last and the best (with best validation metric) checkpoint.
bash tools/dist_train.sh configs/posec3d/slowonly_r50_gym/joint.py 8 --validate --test-last --test-best
```

可以使用以下命令来测试模型。

```shell
bash tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${NUM_GPUS} [optional arguments]
# For example: test PoseC3D on FineGYM (HRNet 2D skeleton, Joint Modality) with metrics `top_k_accuracy` and `mean_class_accuracy`, and dump the result to `result.pkl`.
bash tools/dist_test.sh configs/posec3d/slowonly_r50_gym/joint.py checkpoints/SOME_CHECKPOINT.pth 8 --eval top_k_accuracy mean_class_accuracy --out result.pkl
```