# filename: tf_nn.py
# author: kris bukovi
# last modified: July 24, 2018


from openpyxl import load_workbook
import pandas as pd

def load_dataset():

    lat = []
    lon = []
    ave = []
    limit = []
    
    # load workbook
    wb = load_workbook('test.xlsx')

    # get first sheet name
    first_sheet = wb.sheetnames[0]

    # load worksheet
    ws = wb[first_sheet]

    for i in range(4, 849):

        # store latitude
        lat.append(ws['E' + str(i)].value)

        # store longitude
        lon.append(ws['F' + str(i)].value)

        # store average of draws
        ave.append(ws['L' + str(i)].value)

        # store over limit value
        limit.append(ws['M' + str(i)].value)

    # display locations on chart
    df = pd.DataFrame({'latitude': lat, 'longitude': lon, 'average': ave, 'over limit?': limit})
    print(df)




#def random_mini_batches(X, Y, mini_batch_size = 64, seed = 0):

#def convert_to_one_hot(Y, C):

#def predict(X, parameters):

#def forward_propagation_for_predict(X, parameters):

#def one_hot_matrix(labels, C):

#def ones(shape):

#def create_placeholders(n_x, n_y):

#def initialize_parameters():

#def forward_propagation(X, parameters):

#def compute_cost(Z3, Y):

#def model(X_train, Y_train, X_test, Y_test, learning_rate = 0.0001,
            #num_epochs = 1500, minibatch_size = 32, print_cost = True):

load_dataset()

