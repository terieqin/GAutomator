from wpyscripts.tools.basic_operator import *

def test():
    engine=manager.get_engine()
    logger=manager.get_logger()

    version=engine.get_sdk_version()
    logger.debug("Version Information : {0}".format(version))

    scene=engine.get_scene()
    logger.debug("Scene :   {0}".format(scene))

    sample_button=engine.find_element("/Canvas/Button")
    logger.debug("Button : {0}".format(sample_button))
	#engine.click(sample_button)
    screen_shot_click(sample_button)

if __name__=="__main__":
    test()
