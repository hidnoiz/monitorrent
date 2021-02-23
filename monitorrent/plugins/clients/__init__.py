from monitorrent.plugins.trackers import Topic


class TopicSettings(object):
    download_dir = None
    download_only_last_n_files = None

    def __init__(self, download_dir, download_only_last_n_files=None):
        """
        :type download_dir: str | None
        """
        super(TopicSettings, self).__init__()
        self.download_dir = download_dir
        self.download_only_last_n_files = download_only_last_n_files

    @staticmethod
    def from_topic(topic):
        """
        :type topic: Topic
        """
        return TopicSettings(topic.download_dir)
