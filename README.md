August 17, 2025
C964: Computer Science Capstone

Task 2 parts A, B, C and D
Part A: Letter of Transmittal	2
Proposition Letter	2
Part B: Project Proposal Plan	4
Project Summary	4
Data Summary	4
Implementation	5
Timeline	6
Evaluation Plan	7
Costs	8
Part C: Application	10
Part D: Post-implementation Report	11
Solution Summary	11
Data Summary	11
Machine Learning	11
Validation	11
Visualizations	12
User Guide	14
Reference Page	15


 
Part A: Letter of Transmittal 
Proposition Letter

7/22/2025
 
NW Realtors Executive Board
NW Realtors
123 ABC St.
 
Dear NW Realtors CEO, 
	NW Realtors depends on the accuracy of its housing price prediction methods but is falling short of performance goals. The current prediction is done manually and leaves much room for inaccuracy. Weak price predictions have led to negative returns on properties. The manual process is also time consuming and repetitive. The housing price prediction method is currently setting back decision making ability. With a more accurate and efficient method, houses could be more accurately price estimated allowing for improved investment decisions.
This issue should be remedied using Machine Learning. This will allow for a standardized and efficient process for price prediction. Employees will be able to accurately estimate housing prices within minutes using a simple desktop application. This will enable realtors to make informed decisions on potential listings based on entering characteristics of the house. Customers will benefit from receiving a more accurate price prediction by having financial assurance. They will also benefit from receiving fast quotes, avoiding long wait times without sacrificing accuracy.
The price predictor will be a simple stand-alone application. Realtors will have the app installed to their work devices. Upon opening the application, a simple form requiring info about the house will appear. After entering the information, the predicted price will be provided. The Machine Learning method used will gauge the influence of different attributes of a house on its price. Based on the most entered information an estimation will be calculated in a matter of moments and viewable in the application.
The dataset used to develop the Machine Learning model will be based on housing data from the Seattle area from 2022. The dataset includes details like the number of bedrooms and bathrooms, as well as the size of the unit and lot. The most influential factors will be assessed with data analysis prior to developing the prediction model. With roughly 500 various houses in the dataset, it offers a sufficient volume of data for training the model.
The main hypothesis is that a predictive model can be created with at least 10% accuracy error margin. Additionally, an objective of the solution is to achieve at least 70% variable relevancy to the predicted price. These will be tested thoroughly while the model is developed and cyclically improved.
The Agile methodology will be adopted for this project, allowing for iterative changes to be made as necessary. By developing small functions for the application one piece at a time, the project will make steady progress with little room for error oversight. Tasks will be assigned every week based on a consensus of what most important and core to the applications purpose.
The budget for production will be capped at $500,000 with a 6-month deadline. This will include the salary of 3 programmers, 3 data analysts, 2 project managers, 2 data security specialists, 2 hardware engineers, and 12 new MacBook Pros.
This will have positive impact on NW Realtors in multiple ways. By providing more accurate price predictions investment decisions will be more likely profitable. Additionally, with the process costing less time, productivity rates will increase.
All team members will be informed on how to handle sensitive data. Should any Personally Identifiable Information (PII) be submitted by a customer or contained in submitted data, it will be redacted as soon as possible. The method of redaction will be deletion of the file and removal of the file from any trash buffer.
With my educational background in Computer Science and Artificial Intelligence, as well as my experience with Machine Learning challenges, my expertise is well suited to this project. I have experience with developing the front and back-end of applications, from design, development, to deployment. My knowledge of the Agile methodology is certified by the certificate I own from Atlassian, the company who developed Jira. With all my experience as a foundation, I fully believe this application will help NW Realtors surpass current growth rates.

Sincerely,
Emmett Heffernan
Emmett Heffernan, Product Manager

 
Part B: Project Proposal Plan
Project Summary
NW Realtors current method for housing price prediction is inaccurate, lengthy, and needs an upgrade. Inaccuracy in the price prediction leads to poorly informed investment and listing decisions and then to lost profit. Additionally, the handwritten manual process is company time that could be saved and spent on more productive tasks. An application leveraging Machine Learning will surpass the ability of the current method and alleviate all issues stemming from the current method.

The stockholders and employees of NW Realtors need to increase profit and company growth, as well as provide accurate price predictions to clients to uphold their reputation. Accurately predicting the price of a listed property is a core function to a strong realty firm and NW Realtors depends on this function in many ways.
The deliverables of the project include:
-	A visualization of the data which will provide proof that the predictive attributes of a house relate to its price.
-	A formal statistical report defining percentage scores for accuracy related to margin of error in price prediction, and relevancy of the predictive attributes to the price.
-	A working executable of the application with the pretrained model integrated.
-	A fully documented user guide.

This Machine Learning application will trigger multiple positive changes for NW Realtors. The first being shear outperformance of the old method, in terms of both accuracy and efficiency. Better investment decisions will be enabled by the refined accuracy of the price prediction. The rate of profit will increase due to the increase of productivity which will be triggered by the efficiency of the application. The application will save time and make money for the company.
Data Summary
The dataset will be sourced from Kaggle.com (Cortinhas, 2022). Kaggle provides a built-in download function for its dataset, allowing the user to view files before downloading. The Python library Pandas will be used to store the data in a way accessible to the Machine Learning model.

Using various Python libraries, the dataset will first be normalized. Once normalized dataset will be split with 80% used for training, and the remaining 20% used for testing during development. The dataset may be further normalized depending on the performance of the model through each iteration.

The data comes from a real dataset of houses sold between August and December in 2022 around the Seattle, WA area. The data include the sold price and several physical features, allowing for the developers to prove statistical correlation. Using Python, anomalies will be handled by removing null values, outliers, dirty or messy data, and any other anomalies detected. Units of measurement will be standardized with all acreage values converted to square footage.

From an ethical perspective, the dataset does not include any Personally Identifiable Information (PII) and therefore does not contain any data considered sensitive. From a legal perspective, the license of the dataset is CC0: Public Domain, meaning it can be used in any way including commercial purpose. 
Implementation
The SEMMA methodology will be followed for the completion of this project. SEMMA means: Sample, Explore, Modify, Model, Assess. 
-	Sample: The dataset will be split with 80% for training and 20% for testing.

-	Explore: The dataset will be inspected for anomalies and cleaned accordingly. Data visualizations (correlation heatmap, etc.) will be created to identify which features influence price the most. This step will unveil trends of the dataset.

-	Modify: The dataset at this point may be grouped by property type, or other features found to be influential.  All values with acreage as the unit will be converted to square footage. 

-	Model: The Machine Learning model will be fitted to the most predictive features, to the training and testing partitions of the data. Once the model is connected to the right variables and the dataset it will be trained.

-	Assess: After the model is trained results will be validated with statistical testing. The tests will evaluate based on a percentage what the margin of error is for the prediction, as well as how well the features correlate to the price. Both values will range from 0-100%.

The tasks required for implementation in chronological order are:
o	Extract and inspect data.
o	Clean and normalize data.
o	Create visualizations and observe trends.
o	Develop predictive model and fit the model based on trends observed.
o	Test and evaluate the accuracy of the model’s prediction.
o	Improve model based on performance.
o	Re-fit the model and test again.
o	Create extra test cases to validate the model.
o	Conduct user testing among NW Realtors employees.
o	Create final presentation and launch first deployment.
Timeline
Milestone or deliverable	Project Dependencies	Resources	Start and End Date	Duration
Dataset is fully prepared for model development.	Extract and inspect data. Clean and normalize data.
	Kaggle dataset, Pycharm, developer workstations, Python3, Python library: Pandas, re.	Start: 8/1/2025
End: 8/29/2025	4 Weeks
Create correlation heatmap to evaluate correlation between each house feature and house price.	Dataset is fully prepared, populated, and normalized.	Python library: Pandas, Seaborn	Start: 8/29/25
End: 9/12/2025	2 Weeks
First iteration of the model is complete.	Model is developed and fitted with most correlated features. Model accuracy and relevancy scores are evaluated.	Python library: Pandas, Scikit-Learn	Start: 9/12/2025
End: 10/10/2025	4 Weeks
Second model iteration complete.	Model is re-fitted and tested again to improve accuracy. Test cases are created to further ensure the models accuracy.	Python library: Pandas, Scikit-Learn, Seaborn	Start: 10/10/2025
End: 11/21/2025	6 Weeks
Final presentation of model is complete, and model is deployed.	User testing is conducted and recorded based on satisfaction percentage. Final presentation and summary report are created. Python file is turned into an executable file. 	Python libraries: (Pandas, Seaborn, Scikit-Learn),
Google slides	Start: 12/1/2025
End: 1/1/2026	4 Weeks

Evaluation Plan
The criteria to be evaluated for the project’s success during development will be:
-	Prediction Accuracy: The model will achieve at most 10% error margin for the MAPE score of the prediction.

-	Model Fitness: The R2 value of the prediction will reach at least 70%, meaning 70% correlation between the predictive features and the price.

-	Model Transparency: There will be explainable correlation between variables, and all variables included in the model are clearly understood.


The criteria for validation upon completion of the project includes:
-	A user satisfaction rating of over 70% recorded during user-testing.

-	The model’s maximum allowed error, measured by MAPE score, will reach below 10%.

-	The R2 score of the prediction will reach at higher than 72%.

Costs 
Resource	Description	Cost
Software Development Team	3 Programmers at $40/Hour.
960 hours per programmer.	$115,200
Data Analysts Team	3 Data Analysts
at $38/Hour.
960 hours per analysts.	$109,440
Project Management Team	2 Project Managers
at $45/Hour.
960 hours per manager.	$86,400
Data Security Team	2 Data Security Specialists
at $42/Hour.
960 hours per specialist.	$80,640
Hardware Engineering Team	2 Hardware Engineers
at $44/Hour.
960 hours per engineer.	$84,480
Sprint Meetings	Meeting Cost Associated with Employee attendance: 1 Lead from each team plus two Project Managers.
Meeting duration: 1 Hour.
Meeting Count: 12 meetings.	$3,048
Office Supplies	One 14-inch MacBookPro ($1,599) per each of the 12 employees.	$19,188
IDE	PyCharm 2024.1.4 (Community Edition)
Build #PC-241.18034.82, built on June 24, 2024
Runtime version: 17.0.11+1-b1207.24 x86_64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Metal Rendering is ON
Non-Bundled Plugins:
  com.intellij.ml.llm (241.18034.12)	$0
	Total	$498,396

Part C: Application
 
Part D: Post-implementation Report
Solution Summary
The inefficient price prediction method of NW Realtors was causing inaccuracies and long wait times for housing price predictions. The solution developed to remedy this has utilized the Decision Tree Regression algorithm to detect co-linear relationships between attributes of a house and its price. The predictive model was trained to use the number of bedrooms, bathrooms, and the square footage of the house to predict its price. The predictions generated outperform the old method with higher accuracy, and near instantaneous results.
Data Summary
The raw data was downloaded directly from Kaggle.com (Cortinhas, 2022). In the design phase all rows with null values were removed, and all size units were converted to square footage. In the development phase the correlation of each housing attribute to housing price was analyzed with a correlation heatmap. Columns with a low correlation score were dropped. Next, the most meaningful columns were inspected for outliers. After outlier removal, the training dataset was complete. During the maintenance phase, the steps of the development phase were repeated to increase relevancy of all data points.
Machine Learning
The method used was a Decision Tree Regression algorithm. This is a predictive algorithm which recursively splits the dataset into subsections until the max amount is met. It provides predictions of a target variable and metrics for accuracy.

The method was developed using iterations of testing. First the model was instantiated with the ‘DecisionTreeRegressor’ method from the sci-kit learn library. Next, key attributes were set. The ‘random_state’ attribute was set to 1, this allows the model to have consistency across training iterations. The ‘splitter’ attribute was set to ‘best’ to allow the algorithm to find the optimal splitting method used on the dataset. Lastly, the ‘max_depth’ and ‘min_samples_split’ attributes were tested and adjusted iteratively to minimize the error margin and increase predictive correlation scores.

This model was selected and developed for its easy interpretability and simplistic yet adaptable nature. Without the need for feature scaling, its setup is quick and effective compared to other predictive models. This model also does a good job of handling datasets which may not have explicit linearly defined pattern, allowing it to adapt to nuanced real estate data.
Validation 
The Decision Tree Regressor model is a supervised learning method.

The methods used for validating the model’s performance are provided in the sci-kit learn library’s metrics module. This module provides a plethora of methods for validation centered around different error calculations.

The validation methods of the model’s performance include Mean Accuracy Percentage Error (MAPE) and R2 tests. MAPE provides the model’s margin of error for predictive accuracy and R2 provides a score for the correlation of the predictive features for the housing prices.

 
Visualizations
The following visualizations were created and are contained within the project file; however, they are commented out for functional purposes. These visualizations were used in the development of the model and are more reflective of the cleaned dataset as opposed to the model’s performance.   
User Guide
1.	Download the project folder named ‘HousingPricePredictor’ to the desktop.
2.	Enter ‘PyCharm Community Download’ any search engine and select the correct version for the appropriate operating system using the hyperlink from jetbrains.com.
3.	Install PyCharm to the desktop.
4.	Open PyCharm, from the ‘file’ dropdown menu, select ‘open’ and navigate to the project folder on the desktop.
5.	Run the script and follow the prompts.
6.	Enter the number of bedrooms, bathrooms, and the size in square footage of the property.
7.	Review the price prediction and answer ‘yes’ or ‘no’ to the final prompt ‘Would you like to make another estimate?’.
 
Reference Page
Cortinhas, Samuel. “House Price Prediction - Seattle.” Kaggle, 24 Dec. 2022, www.kaggle.com/datasets/samuelcortinhas/house-price-prediction-seattle. 

