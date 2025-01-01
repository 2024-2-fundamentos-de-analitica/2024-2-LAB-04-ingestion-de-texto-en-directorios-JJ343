# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import pandas as pd

    # Función para procesar un directorio y generar un DataFrame
    def generate_dataset(input_folder):
        data = []
        for sentiment in ["positive", "negative", "neutral"]:
        
            sentiment_path = f"{input_folder}/{sentiment}"  
        
        # Verificar si el directorio existe
            if not os.path.exists(sentiment_path):
             raise FileNotFoundError(f"No se encontró la carpeta: {sentiment_path}")
        
        # Leer los archivos dentro del directorio
            for filename in os.listdir(sentiment_path):
                if filename.endswith(".txt"):
                 file_path = f"{sentiment_path}/{filename}"  
                 with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                        data.append({"phrase": phrase, "target": sentiment}) #esto no deberia ser target, deberia ser sentiment, pero como en el test esta asi ps ya ni modo.
                        
        return pd.DataFrame(data)

# Rutas fijas para train y test
    train_input_folder = "files/input/train"
    test_input_folder = "files/input/test"
    output_folder = "files/output"

# Crear carpeta "output" si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# Generar el dataset para train
    train_dataset = generate_dataset(train_input_folder)
    train_output_path = f"{output_folder}/train_dataset.csv"
    train_dataset.to_csv(train_output_path, index=False)

# Generar el dataset para test
    test_dataset = generate_dataset(test_input_folder)
    test_output_path = f"{output_folder}/test_dataset.csv"
    test_dataset.to_csv(test_output_path, index=False)

    print(f"Archivos generados en la carpeta '{output_folder}':")
    print(f"- {train_output_path}")
    print(f"- {test_output_path}")
pregunta_01()
