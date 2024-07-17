package fun.wuziran.gblogapi.mapper;

import fun.wuziran.gblogapi.entity.About;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Description 关于我 mapper 接口
 * @Author Geralt
 * @Date 2024/7/17
 */
@Mapper
@Repository
public interface AboutMapper {
    List<About> getList();

    int updateAbout(String nameEn, String value);

    String getAboutCommentEnabled();
}
