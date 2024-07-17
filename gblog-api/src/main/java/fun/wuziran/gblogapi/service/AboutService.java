package fun.wuziran.gblogapi.service;

import java.util.Map;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */
public interface AboutService {
    Map<String, String> getAboutInfo();

    Map<String, String> getAboutSetting();

    void updateAbout(Map<String, String> map);

    boolean getAboutCommentEnabled();
}