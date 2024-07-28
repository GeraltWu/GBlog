package fun.wuziran.gblogapi.model.vo;

/**
 * @Description 标签数量 model，作为TagMapper.getTagBlogCount的返回对象
 * @Author Geralt
 * @Date 2024/7/17
 */
public class TagBlogCount {
    private Long id;
    private String name;//标签名
    private Integer value;//标签下博客数量
}
