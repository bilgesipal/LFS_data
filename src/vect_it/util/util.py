import os
import datetime


class ParamServer(object):
    home_path = None
    output_folder = None
    run_vectorizer = None
    data_path = None


    @staticmethod
    def init(experiment_config):
        ParamServer.home_path = experiment_config.home_path
        ParamServer.run_vectorizer = experiment_config.run_vectorizer
        ParamServer.data_path = experiment_config.data_path




class PathServer(object):
    experiment_config_file_path =None
    home_path = None
    config_path = None
    output_path = None
    output_folder_id = None
    log_folder_path = None

    @staticmethod
    def init(experiment_config, experiment_config_file_path, output_folder_id =None):
       PathServer.log_name = datetime.datetime.now().strftime("%Y-%m-%d")
       PathServer.experiment_config_file_path = experiment_config_file_path

       if experiment_config.home_path:
           PathServer.home_path = experiment_config.home_path
       else:
           PathServer.home_path = os.getcwd()

       base_path = PathServer.home_path


       PathServer.config_path = os.path.join(base_path, "config")
       PathServer.data_path = os.path.join(base_path, "data")

       if not output_folder_id:
           PathServer.output_path = os.path.join(base_path, "output")
           PathServer.output_folder_name = PathServer._create_output_folder(PathServer.output_path)
           PathServer.output_folder_path = os.path.join(PathServer.output_path, PathServer.output_folder_name)

       else:
           PathServer.output_folder_name = output_folder_id

       PathServer.log_folder_path = os.path.join(PathServer.output_folder_path, PathServer.log_name)
       PathServer._create_log_folder(PathServer.log_folder_path)


    @staticmethod
    def _create_output_folder(output_path):
        # Check if the output folder exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            return "R0"
        else:
            i = 0
            while True:
                i += 1
                new_output_folder = f"R{i}"
                new_output_path = os.path.join(output_path, new_output_folder)
                if not os.path.exists(new_output_path):
                    os.makedirs(new_output_path)
                    return new_output_folder

    @staticmethod
    def _create_log_folder( output_folder_path):
        log_folder_path = output_folder_path
        print(output_folder_path)
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)




