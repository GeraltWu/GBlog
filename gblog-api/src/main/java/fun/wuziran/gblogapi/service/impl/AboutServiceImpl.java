package fun.wuziran.gblogapi.service.impl;

import fun.wuziran.gblogapi.entity.About;
import fun.wuziran.gblogapi.mapper.AboutMapper;
import fun.wuziran.gblogapi.service.AboutService;
import fun.wuziran.gblogapi.util.markdown.MarkdownUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Description 关于我service实现类
 * @Author Geralt
 * @Date 2024/7/17
 */

@Service
public class AboutServiceImpl implements AboutService {
    @Autowired
    AboutMapper aboutMapper;
    @Override
    public Map<String, String> getAboutInfo() {
        List<About> abouts = aboutMapper.getList();
        Map<String, String> aboutInfoMap = new HashMap<>(16);
        for (About about : abouts) {
            if ("content".equals(about.getNameEn())) {
                about.setValue(MarkdownUtils.markdownToHtmlExtensions(about.getValue()));
            }
            aboutInfoMap.put(about.getNameEn(), about.getValue());
        }
        return aboutInfoMap;
    }


    @Override
    public Map<String, String> getAboutSetting() {
        List<About> abouts = aboutMapper.getList();
        Map<String, String> map = new HashMap<>(16);
        for (About about : abouts) {
            map.put(about.getNameEn(), about.getValue());
        }
        return map;
    }

    @Override
    public void updateAbout(Map<String, String> map) {

    }

    @Override
    public boolean getAboutCommentEnabled() {
        return false;
    }
}
