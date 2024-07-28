package fun.wuziran.gblogapi.model.vo;

import lombok.Data;

/**
 * @Description 归档页面博客简要信息
 * @Author Geralt
 * @Date 2024/7/17
 */

@Data
public class ArchiveBlog {
    private Long id;
    private String title;
    private String day;
    private String password;
    private Boolean privacy;
}
