package fun.wuziran.gblogapi.model.vo;

import lombok.Data;

/**
 * @Description 最新的推荐博客
 * @Author Geralt
 * @Date 2024/7/17
 */

@Data
public class NewBlog {
    private Long id;
    private String title;
    private String password;
    private Boolean privacy;
}
