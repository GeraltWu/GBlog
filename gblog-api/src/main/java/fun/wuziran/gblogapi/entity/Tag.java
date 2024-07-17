package fun.wuziran.gblogapi.entity;

import lombok.Data;

import java.util.ArrayList;
import java.util.List;

/**
 * @Description 博客标签
 * @Author Geralt
 * @Date 2024/7/17
 */
@Data
public class Tag {
    private Long id;
    private String name;//标签名称
    private String color;//标签颜色(与Semantic UI提供的颜色对应，可选)
    private List<Blog> blogs = new ArrayList<>();//该标签下的博客文章
}
