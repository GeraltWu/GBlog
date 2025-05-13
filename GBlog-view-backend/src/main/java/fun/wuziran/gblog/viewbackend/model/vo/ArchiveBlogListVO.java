package fun.wuziran.gblog.viewbackend.model.vo;

import lombok.Data;
import java.util.List;

/**
 * @Description 归档博客列表VO
 * @Author Geralt
 * @Date 2025/1/10
 */
@Data
public class ArchiveBlogListVO {
    // 博客总数
    private int totalQuantity;
    // 按月份归档的博客列表
    private List<ArchiveBlogMonthlyVO> list;
} 