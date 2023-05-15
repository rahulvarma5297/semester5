# Web Page Phishing Detection using Random Forest
# Use training.csv for training
# First Train the model using training.csv
# Next Use testing.csv for testing the model
# print the accuracy, precision, recall and f1-score
# Pre process the data before training and testing for better results

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Read the training data
training_data = pd.read_csv("training.csv")

# Read the testing data
testing_data = pd.read_csv('testing.csv')

# Removing the URL column from the data
training_data = training_data.drop('url', axis=1)
testing_data = testing_data.drop('url', axis=1)

# Replace the missing values with 0
training_data = training_data.fillna(0)
testing_data = testing_data.fillna(0)

# lengthm_hostname,ip,nb_dots,nb_hyphens,nb_at,nb_qm,nb_and,
# nb_or,nb_eq,nb_underscore,nb_tilde,nb_percent,nb_slash,nb_star,
# nb_colon,nb_comma,nb_semicolumn,nb_dollar,nb_space,nb_www,nb_com,
# nb_dslash,http_in_path,https_token,ratio_digits_url,ratio_digits_host,
# punycode,port,tld_in_path,tld_in_subdomain,abnormal_subdomain,nb_subdomains
# ,prefix_suffix,random_domain,shortening_service,path_extension,
# nb_redirection,nb_external_redirection,length_words_raw,char_repeat
# ,shortest_words_raw,shortest_word_host,shortest_word_path,longest_words_raw,
# longest_word_host,longest_word_path,avg_words_raw,avg_word_host,avg_word_path,
# phish_hints,domain_in_brand,brand_in_subdomain,brand_in_path,suspecious_tld,
# statistical_report,nb_hyperlinks,ratio_intHyperlinks,ratio_extHyperlinks,
# ratio_nullHyperlinks,nb_extCSS,ratio_intRedirection,ratio_extRedirection,
# ratio_intErrors,ratio_extErrors,login_form,external_favicon,links_in_tags,
# submit_email,ratio_intMedia,ratio_extMedia,sfh,iframe,popup_window,
# safe_anchor,onmouseover,right_clic,empty_title,domain_in_title,
# domain_with_copyright,whois_registered_domain,domain_registration_length,
# domain_age,web_traffic,dns_record,google_index,page_rank,status


training_data = training_data.drop('ratio_nullHyperlinks', axis=1)
testing_data = testing_data.drop('ratio_nullHyperlinks', axis=1)

training_data = training_data.drop('google_index', axis=1)
testing_data = testing_data.drop('google_index', axis=1)

training_data = training_data.drop('ratio_intErrors', axis=1)
testing_data = testing_data.drop('ratio_intErrors', axis=1)

training_data = training_data.drop('submit_email', axis=1)
testing_data = testing_data.drop('submit_email', axis=1)


# Create the training and testing arrays
X_train = training_data.iloc[:, 0:-1]
y_train = training_data.iloc[:, -1]
X_test = testing_data.iloc[:, 0:-1]
y_test = testing_data.iloc[:, -1]
clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred, pos_label='phishing'))
print("Recall: ", recall_score(y_test, y_pred, pos_label='phishing'))
print("F1-Score: ", f1_score(y_test, y_pred, pos_label='phishing'))
