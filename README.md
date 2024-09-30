# On the Application of Egocentric Computer Vision to Industrial Inspection

[[`Paper`](https://drive.google.com/file/d/1js-4P-NdWX68ouwjCD6eDOyMhD-a_A6d/view?usp=sharing)] [[`Poster`](https://drive.google.com/file/d/1UrWMS26FOmq9uBtISKIeJSVubGSdUn71/view?usp=sharing)]

**Abstract:** Conventional Industrial Inspection is often carried out with dedicated digitisation and monitoring systems. This approach offers superior accuracy and reliability. However, it poses limitations w.r.t. setup costs and location requirements. Recently, Egocentric Vision has been getting increased attention from the community. We investigate the applicability of egocentric wearable devices for data collection and labelling for classification, detection, segmentation, and defect/anomaly detection use cases. We also explore scenarios where egocentric vision would be superior for data collection and inspection. Our approach involves a multimodal data collection pipeline, where the Subject-Matter Expert (SME) labels and annotates the data in natural language during digitisation, which is then processed to yield an annotated dataset for downstream applications. We also incorporate useful indicators, such as user eye gaze (via wearable glasses) and hand tracking to understand and annotate the regions of interest in the collected data. Our investigation shows a domain gap when generalising the performance of Machine Learning (ML) models trained on egocentric data to allocentric/exocentric use cases. Further, we discuss the limitations and practical use cases of our approach, considering the hardware and power consumption requirements.

![Poster](https://github.com/Vivek9Chavan/ADCM/blob/main/(ECCV2024%20Workshop)%20VISION.jpg)

## Code and resources will be available here soon.

## Acknowledgements

Our code borrows heavily form the following repositories:

https://github.com/facebookresearch/projectaria_tools

https://github.com/facebookresearch/projectaria_eyetracking

<a name="bibtex"></a>
## Citation

If you find our work or any of our materials useful, please cite our papers:
```
@InProceedings{Chavan_2024_ECCVW,
    author    = {Chavan, Vivek and Heimann, Oliver and Kr\"uger, J\"org},
    title     = {On the Application of Egocentric Computer Vision to Industrial Inspection},
    booktitle = {European Conference on Computer Vision (ECCV) Workshops},
    month     = {October},
    year      = {2024}
}
