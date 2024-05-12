# PYSKL

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revisiting-skeleton-based-action-recognition/skeleton-based-action-recognition-on-ntu-rgbd)](https://paperswithcode.com/sota/skeleton-based-action-recognition-on-ntu-rgbd?p=revisiting-skeleton-based-action-recognition)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/dg-stgcn-dynamic-spatial-temporal-modeling/skeleton-based-action-recognition-on-ntu-rgbd-1)](https://paperswithcode.com/sota/skeleton-based-action-recognition-on-ntu-rgbd-1?p=dg-stgcn-dynamic-spatial-temporal-modeling)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/revisiting-skeleton-based-action-recognition/skeleton-based-action-recognition-on-kinetics)](https://paperswithcode.com/sota/skeleton-based-action-recognition-on-kinetics?p=revisiting-skeleton-based-action-recognition)
[\[**Report**\]](https://arxiv.org/abs/2205.09443)

PYSKL 是一个基于 PYTorch 的 SKeLeton 数据的动作识别工具箱。基于骨架的动作识别将支持各种算法。我们基于开源项目 [MMAction2](https://github.com/open-mmlab/mmaction2) 构建了这个项目。

这个repo是 [PoseConv3D](https://arxiv.org/abs/2104.13586) 和 [STGCN++](https://github.com/kennymckormick/pyskl/tree/main/configs/stgcn%2B%2B) 的官方实现。

<div id="wrapper" align="center">
<figure>
  <img src="https://user-images.githubusercontent.com/34324155/123989146-2ecae680-d9fb-11eb-916b-b9db5563a9e5.gif" width="520px">&emsp;
  <img src="https://user-images.githubusercontent.com/34324155/218010909-ccfc89f0-9ed4-4b04-b38d-af7ffe49d2cd.gif" width="290px"><br>
  <p style="font-size:1.2vw;">左图：NTU-RGB+D-120 上的基于骨架的动作识别结果；右图：基于骨架的CPU实时手势识别结果</p>
</figure>
</div>

## 更改日志


- 改进骨架提取脚本([PR](https://github.com/kennymckormick/pyskl/pull/150))。现在它支持非分布式骨架提取和k400样式(**2023-03-20**)。
- 支持 PyTorch 2.0：当设置 `--compile` 用于训练/测试脚本并使用`torch.__version__ >= 'v2.0.0'`，将在训练/测试之前使用 `torch.compile` 编译模型。实验功能，绝对无性能保证(**2023-03-16**)。
- 使用 ST-GCN++ 提供基于骨架的动作识别的实时手势识别演示，查看 [Demo](./demo/demo.md) 了解更多细节和说明(**2023-02-10**)。
- 提供脚本 [scripts](./examples/inference_speed.ipynb) 来估计每个模型的推理速度(**2022-12-30**)。
- 支持 [RGBPoseConv3D](https://arxiv.org/abs/2104.13586)，一个基于 RGB 和人体骨架的双流 3D-CNN 动作识别。按照指南 [guide](./configs/rgbpose_conv3d/README.md) 在 NTURGB+D 上训练和测试 RGBPoseConv3D（**2022-12-29**)。

## Supported Algorithms

- [x] [DG-STGCN (Arxiv)](https://arxiv.org/abs/2210.05895) [[MODELZOO](/configs/dgstgcn/README.md)]
- [x] [ST-GCN (AAAI 2018)](https://arxiv.org/abs/1801.07455) [[MODELZOO](/configs/stgcn/README.md)]
- [x] [ST-GCN++ (ACMMM 2022)](https://arxiv.org/abs/2205.09443) [[MODELZOO](/configs/stgcn++/README.md)]
- [x] [PoseConv3D (CVPR 2022 Oral)](https://arxiv.org/abs/2104.13586) [[MODELZOO](/configs/posec3d/README.md)]
- [x] [AAGCN (TIP)](https://arxiv.org/abs/1912.06971) [[MODELZOO](/configs/aagcn/README.md)]
- [x] [MS-G3D (CVPR 2020 Oral)](https://arxiv.org/abs/2003.14111) [[MODELZOO](/configs/msg3d/README.md)]
- [x] [CTR-GCN (ICCV 2021)](https://arxiv.org/abs/2107.12213) [[MODELZOO](/configs/ctrgcn/README.md)]

## Supported Skeleton Datasets

- [x] [NTURGB+D (CVPR 2016)](https://arxiv.org/abs/1604.02808) and [NTURGB+D 120 (TPAMI 2019)](https://arxiv.org/abs/1905.04757)
- [x] [Kinetics 400 (CVPR 2017)](https://arxiv.org/abs/1705.06950)
- [x] [UCF101 (ArXiv 2012)](https://arxiv.org/pdf/1212.0402.pdf)
- [x] [HMDB51 (ICCV 2021)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6126543)
- [x] [FineGYM (CVPR 2020)](https://arxiv.org/abs/2004.06704)
- [x] [Diving48 (ECCV 2018)](https://openaccess.thecvf.com/content_ECCV_2018/papers/Yingwei_Li_RESOUND_Towards_Action_ECCV_2018_paper.pdf)

## Installation
```shell
git clone https://github.com/kennymckormick/pyskl.git
cd pyskl
# This command runs well with conda 22.9.0, if you are running an early conda version and got some errors, try to update your conda first
conda env create -f pyskl.yaml
conda activate pyskl
pip install -e .
```

## Demo

Check [demo.md](./demo/demo.md).

## Data Preparation

我们为我们支持的每个数据集提供HRNet 2D骨架，并为NTURB+D和NTURB+T 120数据集提供Kinect 3D骨架。要获得人体骨骼标注，你可以：

1. 使用我们预处理的骨架注释：我们直接将所有数据集的处理过的骨架数据作为 pickle 文件提供（可以直接用于训练和测试），查看 [Data Doc](./tools/data/README.md)  以获取标注格式的描述下载链接。
2. 对于 NTURGB+D 3D 骨架，可以从 https://github.com/shahroudy/NTURGB-D 下载官方标注，并使用我们提供的脚本生成处理后的 pickle 文件。生成的文件与提供的 `ntu60_3danno.pkl` 和 `ntu120_3danno.pkl` 相同。有关详细说明，请参阅 [Data Doc](./tools/data/README.md)。
3. 我们还提供了从 RGB 视频中提取 2D HRNet 骨架的脚本，您可以按照 [diving48_example](./examples/extract_diving48_skeleton/diving48_example.ipynb) 从任意 RGB 视频数据集中提取 2D 骨架。

你可以使用 [vis_skeleton](/demo/vis_skeleton.ipynb) 可视化提供的骨架数据。

## Training & Testing

您可以使用以下命令进行训练和测试。基本上，我们支持在具有多个 GPU 的单个服务器上进行分布式训练。

```shell
# Training
bash tools/dist_train.sh {config_name} {num_gpus} {other_options}
# Testing
bash tools/dist_test.sh {config_name} {checkpoint} {num_gpus} --out {output_file} --eval top_k_accuracy mean_class_accuracy
```

有关具体示例，请访问我们支持的每个特定算法的 README 文件。

## Citation

如果您在研究中使用 PYSKL 或希望参考 Model Zoo 中发布的基线结果，请使用以下 BibTeX 条目和与您使用的特定算法相对应的 BibTeX 条目。

```BibTeX
@inproceedings{duan2022pyskl,
  title={Pyskl: Towards good practices for skeleton action recognition},
  author={Duan, Haodong and Wang, Jiaqi and Chen, Kai and Lin, Dahua},
  booktitle={Proceedings of the 30th ACM International Conference on Multimedia},
  pages={7351--7354},
  year={2022}
}
```

## Contributing

PYSKL is an OpenSource Project under the Apache2 license. Any contribution from the community to improve PYSKL is appreciated. For **significant** contributions (like supporting a novel & important task), a corresponding part will be added to our updated tech report, while the contributor will also be added to the author list.

Any user can open a PR to contribute to PYSKL. The PR will be reviewed before being merged into the master branch. If you want to open a **large** PR in PYSKL, you are recommended to first reach me (via my email dhd.efz@gmail.com) to discuss the design, which helps to save large amounts of time in the reviewing stage.

## Contact

For any questions, feel free to contact: dhd.efz@gmail.com
