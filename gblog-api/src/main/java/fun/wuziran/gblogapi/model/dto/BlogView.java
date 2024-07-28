package fun.wuziran.gblogapi.model.dto;

import lombok.Data;

/**
 * @Description 博客浏览量
 * @Author Geralt
 * @Date 2024/7/17
 */
@Data
public class BlogView {
    private Long id;
    private Integer views;
}
