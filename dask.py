# dask bag

from dask import bag

# get image dimensions
def get_dims(file):
    img = cv2.imread(file)
    h,w = img.shape[:2]
    return h,w

# parallelize
filepath = '../input/stage_1_test_images/'
filelist = [filepath + f for f in os.listdir(filepath)]
dimsbag = bag.from_sequence(filelist).map(get_dims)
with diagnostics.ProgressBar():
    dims = dimsbag.compute()
