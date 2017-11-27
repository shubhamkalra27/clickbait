from sklearn.externals import joblib
import os

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir,r'static',r'model_1.pkl')
model_1 = joblib.load(model_path)


def scoring(headline):
    """
    scoring function - takes in a headline and returns a dictionary
    :param headline:
    :return:
    """
    pred_score = model_1.predict_proba([headline])[0]
    if ((pred_score[1]*100 > 40) & ((pred_score[1]*100 < 60))):
        tag = 'Not Sure'
        color = 'is-warning'
    elif (pred_score[1]*100 > 60):
        tag = 'Baity'
        color = 'is-danger'
    else:
        tag = 'Looks Safe'
        color = 'is-primary'

    prob = {'P-clickbate': round(pred_score[1],3), 'P-notClickbate': round(pred_score[0],3), 'tag': tag, 'color':color}
    return prob

if __name__ == "__main__":
    result = scoring('6 Possible Hurdles For The GOP Tax Plan')
    print(result)