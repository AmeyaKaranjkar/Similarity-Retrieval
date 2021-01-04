A. Initially included files-
	* use_model.py
	* use_cosine_similarity.py
	* use_model_accuracy.py
	* sbert_model.py
	* sbert_encode.py
	* sbert_cosine_similarity.py
	* sbert_model_accuracy.py
	* preprocess_query.py
	* accuracy.py
	* answer_query.py
	* README.txt
	* g23-final.pdf
	* g23-presentation.pdf
		
B. Language, platform, and packages/modules and dependencies-
	> OS: Ubuntu 20.04.1 LTS
	> Language: Python 3.8.3
	> Packages:
		1. tensorflow
		2. pandas
		3. numpy
		4. math (built-in)
		5. pickle
		6. re
		7. nltk
		8. nltk punkt
		9. tensorflow-hub
		10. sentence-transformers
		11. demoji
		12. nltk stopwords
		13. nltk wordnet
		14. demoji
		15. unidecode
		16. webbrowser
		17. tkinter
		
C. Workflow
	1. use_model.py
	Generates the embeddings of the questions in the corpus using the Universal Sentence Encoder (USE) model and saves the same as 'use_embedding.data'.
	
	2. use_cosine_similarity.py
	Generates similarity scores for each query with each question. Hence for each query we will have a similarity vector of size 34,235 as we have 34,235 questions in the corpus. Hence for each of the 440 questions in the test dataset we will have similarity scores with each question in the corpus. This is saved as 'use_cosine_simscores.data'.
	
	3. use_model_accuracy.py
	This computes the accuracy of the USE model with the cosine similarity as similarity metric using the similarity scores for each test query present in 'use_cosine_simscores.data'.
	
	4. sbert_model.py
	This file simply imports the pre-trained sbert model and saves the model as 'sbert_model.sav'.
	
	5. sbert_encode.py
	This file generates the embeddings of the questions in the corpus using the Sentence-BERT model and saves the same as 'sbert_embedding.data'.
	
	6. sbert_cosine_similarity.py
	Generates similarity scores for each query with each question. This is exactly same as that for USE model in 'use_cosine_similarity' the only difference being the embeddings of the questions and the test queries. This is saved as 'sbert_cosine_simscores.data'.
	
	7. sbert_model_accuracy.py
	This file computes the accuracy of the SBERT model with the cosine similarity as the similarity metric using the similarity scores for each test query present in 'sbert_cosine_simscores.data'.
	
	8. accuracy.py
	This file computes the accuracy of the combined model.
	
	9. answer_query.py
	This file generates a GUI, which takes a user query as input and outputs the 7 most similar questions to the user query predicted by the USE model with cosine similarity measure.

D. Helper files
	1. preprocess_query.py - This file is used to preprocess the user query before it is embedded by the USE model.
	
* GitHub link for the entire project- https://github.com/AmeyaKaranjkar/Similarity-Retrieval




