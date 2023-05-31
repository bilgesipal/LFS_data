import os
import cloudpickle
import time


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from vect_it.logger.logger import Logger
from vect_it.config.config import ModelConfig, ExperimentConfig
from vect_it.util.util import PathServer, ParamServer


def read_experiments():
    pass


def process_pickle(obj, file_path):
    with open(file_path, 'wb') as file:
        cloudpickle.dump(obj, file)


def process_config(config_list, logger):
    logger.log_msg('INFO', 'It is done')
    for config in config_list:
        if config == 'model':
            model_config = ModelConfig(os.path.join(PathServer.config_path, 'model_config.ini'))
            return model_config
        else:
            logger.log_msg('ERROR', 'It is not done')


def process_read_data(logger):
    logger.log_msg('INFO', 'data reading is done')
    text_path = os.path.join(PathServer.data_path, 'data.txt')
    fd = open(text_path)
    content = fd.read()
    corpus = content.split(',')
    fd.close()
    return corpus


def process_tfidfvect_it(model_config, corpus, logger):
    '''
    tfidf vectorizatrion is processed

    :param model_config:
    :param corpus:
    :param logger:
    :return:
    '''
    logger.log_msg('INFO', 'tfidf vectorization is done')
    vectorizer = TfidfVectorizer(analyzer=model_config.analyzer)

    vectorizer.fit_transform(corpus)
    names = vectorizer.get_feature_names_out()
    file_path = os.path. join(PathServer.log_folder_path, 'tfidf.pkl')
    process_pickle(names, file_path)


def process_countvect_it(model_config, corpus, logger):
    start_time = time.time()
    logger.log_msg('INFO', ' Bow  is done')
    vectorizer = CountVectorizer(analyzer=model_config.analyzer, lowercase=bool(model_config.lower_case))
    vectorizer.fit_transform(corpus)
    names = vectorizer.get_feature_names_out()
    file_path = os.path.join(PathServer.log_folder_path, 'bow.pkl')
    process_pickle(names, file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.log_msg('INFO', f"Elapsed time: {elapsed_time:.2f} seconds")


def main():
    experiment_config_file_path = os.path.join(os.getcwd(), 'experiment/experiment.ini')
    experiment_config = ExperimentConfig(experiment_config_file_path)
    PathServer.init(experiment_config, experiment_config_file_path, output_folder_id=None)
    ParamServer.init(experiment_config)
    log_path = os.path.join(PathServer.log_folder_path, "log_file.txt")
    logger = Logger(log_path)

    config_list = ['model']
    model_config = process_config(config_list, logger)
    corpus = process_read_data(logger)

    if model_config.model == 'bow':
        process_countvect_it(model_config, corpus, logger)
    elif model_config.model == 'tfidf':
        process_tfidfvect_it(model_config, corpus, logger)
    else:
        logger.log_msg('ERROR', 'No such vectorization')
