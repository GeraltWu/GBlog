package fun.wuziran.gblogapi.service.impl;

import fun.wuziran.gblogapi.mapper.AboutMapper;
import fun.wuziran.gblogapi.service.AboutService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */

@Service
public class AboutServiceImpl implements AboutService {
    @Autowired
    AboutMapper aboutMapper;
    @Override
    public Map<String, String> getAboutInfo() {
        return null;
    }

    @Override
    public Map<String, String> getAboutSetting() {
        return null;
    }

    @Override
    public void updateAbout(Map<String, String> map) {

    }

    @Override
    public boolean getAboutCommentEnabled() {
        return false;
    }
}
