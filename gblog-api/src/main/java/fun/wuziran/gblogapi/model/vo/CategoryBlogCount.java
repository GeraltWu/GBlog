package fun.wuziran.gblogapi.model.vo;


import lombok.Data;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */

@Data
public class CategoryBlogCount {
    private Long id;
    private String name;//分类名
    private Integer value;//分类下博客数量
}
