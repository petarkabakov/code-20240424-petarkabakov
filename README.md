# code-20240423-petarkabakov

I start with loading the file using pandas and Python and check the data types and which columns have null values using the .info() method. 

After making sure that the columns, that are highlighted (contract_id, sku, winner_price) have all non-null values. I can proceed with checking if the number of unique contract_id values is the same as the number of rows in the table to make sure that all contract_id values are unique. 

The next step is to create a new column that checks if the winning price is the lowest and if not to exclude it from the data set as per the instructions.

Once the initial data cleaning is done, now is time to remove the outliers from the data. There are many different ways that can be done, however, the best approach will depend on the machine learning model that will be used. Some models like linear regression would be more sensitive to outliers, whereas, more sophisticated ensemble models (e.g. random forest, gradient boosting) would handle outliers better on their own. 

In the example, I will identify the outliers creating a z-score and filtering out all values that are more than +/- 3 z-score. This is subjective and could be influenced by a lot of different assumptions or the data distribution. In summary, what we are doing in this method is making sure that the values that are left are no more than 3 standard deviations plus or minus from the mean of the data set, assuming a normal distribution. 

Question: What automated approaches can you use?
Answer: The automation process in the first instance will be scripting. Creating a simple Python script that can be either executed manually or scheduled to run at a specific time. In the future this could be upgraded to handle more columns or complicated requirements and even combine data from multiple sources. 

Question: What manual tasks would you perform?
Answer: I would try to reduce the manual tasks to a minimum, which would make the process easier to replicate in the future and make it part of a data pipeline. However, the exploration of the data and the first time all the checks and conditions making are manual processes that cannot be avoided.

Question: How would you improve this process long term and how would you build your roadmap?
Answer: That will depend on the data infrastructure in use and the way the data is sourced. In an ideal world, the data would be added to a database or a data lake, from where an automated data pipeline can be built. This is exactly what I have done in my current role on multiple occasions, creating a data pipeline in Azure, that was first developed in Python using pysrak within Data Bricks, and afterwards, scheduled to run on Azure devops. However, similar roadmap and development could be implemented through most cloud providers. 

Question: Would you change anything if you would need to scale this process from a few SKU's to hundreds and thousands.
Answer: Using standard Python scripts would work without any issues for hundreds or even thousands of entries as long we don't have too many columns and the size of the table can be stored in memory. However, with thousands of entries, the size of the table would scale in size very quickly with the addition of new columns which would negatively impact the performance or render the process to outright fail. This would mean that moving the process from a local machine to a server or a cloud environment would be required. 
