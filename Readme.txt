The repository contains 7 files:

1) Photo to which filters are applied;
2) imge_with_filters.py - code overlay filters;
3) The result of applying filters in mp4 format;
4) circle_detector.py - code for finding circles in the photo: Very simple code based on the openCV library, suitable for simple tasks. This can be seen when working with the first 2 test pictures(test_1, test_2). The drop in the quality of processing starts from the 3rd picture(test_3). On a real image of a cell culture, the result is completely disastrous (cells). To improve the work in the future, you can use the Sobel operator or the Canny Algorithm;
4 - 7) Test images.