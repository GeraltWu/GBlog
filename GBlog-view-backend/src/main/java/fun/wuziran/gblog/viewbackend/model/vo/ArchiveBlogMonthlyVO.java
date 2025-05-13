package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;
import java.util.List;

/**
 * @Description 按月归档博客VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class ArchiveBlogMonthlyVO {
    // 归档的月份
    private String month;
    // 该月份下的博客列表
    private List<ArchiveBlogVO> list;
} 