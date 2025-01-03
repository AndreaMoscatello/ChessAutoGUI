# ChessAutoGUI
An AI model build using a NN trained to recognize chess pieces and a autoclicker (pyautogui) designed to make the best moves by itself. The engine is Stockfish 15. As of latest version, the model work only on a Lichess interface and if the player has the white pieces.

The Stockfish engine is not provided in this repository as it can be freely downloaded from the official Stockfish website.

The original chess pieces datasets and the CNN comes from: 
- https://www.kaggle.com/datasets/s4lman/chess-pieces-dataset-85x85/code
- https://www.kaggle.com/code/hasanatlodhi/chess-pieces-identification

The dataset is expanded with the lichess pieces.

Few differences to the CNN has been made just to play around with the parameters. As the model was still not showing a satisfaying accuracy, the key feature to increment the correct classification rate is the binarization of the images before evaluation. 

DISCLAIMER: this project is developed only for entertaing purposes and to further develope my CNN knowledges. It was only used to play againg other computers and never agains human players as this constitutes a cheating device. DO NOT use such a code against any real players on the platform. 
