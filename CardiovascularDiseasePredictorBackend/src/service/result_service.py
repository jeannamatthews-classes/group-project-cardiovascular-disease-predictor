import os
import pickle
import pandas as pd
from io import StringIO

"""
Implements the logic to generate the result for a sample
"""

class ResultService:

    CURRENT_FILE_DIR= os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = "../../resource"
    FEATURE_LIST_FILENAME = 'feature_names.csv'
    MODEL_DIR = "../model"
    RESULT_RESPONSE_CLASS1 = ['ABSENT', 'PRESENT']
    RESULT_RESPONSE_CLASS2 = ['ABSENT', 'HYPERTENSION','CORONARY ARTERY DISEASE',
                            'CARDIOMYOPATHY', 'HEART FAILURE', 'CONGENITAL HEART DISEASE']


    def get_results(self, predict_type, sample_path):
        """
        Get the result of a sample and stores the result in a database.
        The result statement is also returned.
        Inputs:
            predict_type: a string representing the prediction type. Expected values are 1 (class1) and 2 (class2).
            sample_path:  path for the sample
        Outputs:
                result_statement: a string summarizing the result of the analysis
        """
        #get sample
        sample = self.load_sample(sample_path)

        #get prediction
        model = self.load_model(predict_type)                                    #load model
        prediction = model.predict(sample)
        predicted_class = int(prediction[0])

        #interpret prediction
        final_result = self.interpret_result(predict_type, predicted_class)

        return final_result

    def load_sample(self, sample_data):
        """
        load the sample into a dataframe
        Inputs:
            sample_data: string representing the path of the sample
        Outputs:
            sample:  a pandas dataframe representing the inputs from a sample
        """

        try:
             #load sample
             csv_data = StringIO(sample_data)
             sample_df = pd.read_csv(csv_data)

             #load feature names
             resource_path = os.path.join(self.CURRENT_FILE_DIR, self.RESOURCE_DIR)
             expected_features = pd.read_csv(os.path.join(resource_path,
                                              self.FEATURE_LIST_FILENAME))

             #check if all features are valid
             invalid_features = []
             for column in sample_df.columns:
                column = column.strip()
                if(column.upper() not in list(expected_features["Table Heading"])):
                      invalid_features.append(column)

             if(len(invalid_features) > 0):
                print("ERROR: The invalid features below were found in the input file. Please fix the input file.")
                print(invalid_features)
                exit(1)

             #remove spaces in feature names
             sample_df.columns = sample_df.columns.str.strip()

             return sample_df

        except FileNotFoundError:
             print(f"ERROR: The file was not found. Please enter a valid file.")
             exit(1)




    def load_model(self, predict_type):
        """
        Get the model based on prediction type
        Inputs:
            predict_type: a string representing the prediction type. Expected values are 1 (class1) and 2 (class2).
        Outputs:
                tree_model: the model to use for prediction
        """

        #check if a valid predict type is sent
        if(predict_type !=  '1' and predict_type !=  '2'):
            print("ERROR: Invalid Prediction Type. Prediction Type should be 1 or 2.")
            exit(1)

        #get model
        model_file_name = "model_class" + str(predict_type) + ".pkl"
        model_dir_abs_path = os.path.join(self.CURRENT_FILE_DIR, self.MODEL_DIR)
        model_file_path = os.path.join(model_dir_abs_path, model_file_name)
        with open(model_file_path, 'rb') as f:
            model = pickle.load(f)
        return model



    def store_result(self, predict_type, sample, predicted_value):
        """
        Store the result of a sample to the database
        Inputs:
            predict_type: a string representing the prediction type. Expected values are 1 (class1) and 2 (class2).
            sample:  a pandas dataframe representing the inputs from a sample
            predicted_value: a string representing the result of the prediction
        Outputs:
                None
        """
        return 0

    def interpret_result(self, predict_type, predicted_class):
        # interpret prediction
        predicted_value = ""
        if (predict_type == '1'):
            predicted_value = self.RESULT_RESPONSE_CLASS1[predicted_class]
        else:
            predicted_value = self.RESULT_RESPONSE_CLASS2[predicted_class]

        # store result into the database
        #self.store_result(sample, predict_type, predicted_value)

        # generate result statement
        result_statement = ""
        if (predicted_value == 'ABSENT'):
            result_statement = "The sample was found to have a low risk of cardiovascular disease."
        else:
            if (predict_type == '1'):
                result_statement = "The presence of cardiovascular disease was detected in the sample."
            else:
                result_statement = f"The presence of {predicted_value} was detected in the sample."

        return result_statement




#data = 'AGE,GENDER,SMOKING,ALCOHOL, DM, CKD, HB, TLC,PLATELETS, GLUCOSE, UREA, CREATININE, BNP,RAISED CARDIAC ENZYMES, EF,SEVERE ANAEMIA, ANAEMIA,STABLE ANGINA, ACS, STEMI, ATYPICAL CHEST PAIN, HFREF,HFNEF, VALVULAR, CHB, SSS, AKI, CVA INFRACT, CVA BLEED,AF, VT, PSVT, UTI, NEURO CARDIOGENIC SYNCOPE, ORTHOSTATIC,INFECTIVE ENDOCARDITIS, DVT, CARDIOGENIC SHOCK, SHOCK,PULMONARY EMBOLISM, CHEST INFECTION \n0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
#result_service = ResultService()
#print(result_service.interpret_result("2", 5))






