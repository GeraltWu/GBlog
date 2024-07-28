package fun.wuziran.gblogapi.model.vo;

import lombok.Data;

import java.util.List;

/**
 * @Description 分页结果
 * @Author Geralt
 * @Date 2024/7/17
 */

@Data
public class PageResult<T> {
    private Integer totalPage;//总页数
    private List<T> list;//数据

    public PageResult(Integer totalPage, List<T> list) {
        this.totalPage = totalPage;
        this.list = list;
    }
}
