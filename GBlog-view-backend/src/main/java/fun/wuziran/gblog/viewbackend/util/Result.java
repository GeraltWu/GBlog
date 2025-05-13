package fun.wuziran.gblog.viewbackend.util;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/12/22
 */

@NoArgsConstructor
@Getter
@Setter
@ToString
public class Result<T> {
    private Integer code;
    private String msg;
    private T data;

    private Result(Integer code, String msg) {
        this.code = code;
        this.msg = msg;
        this.data = null;
    }

    private Result(Integer code, String msg, T data) {
        this.code = code;
        this.msg = msg;
        this.data = data;
    }

    // 静态方法支持泛型
    public static <T> Result<T> ok(String msg, T data) {
        return new Result<>(200, msg, data);
    }

    public static <T> Result<T> ok(String msg) {
        return new Result<>(200, msg, null);
    }

    public static <T> Result<T> ok(T data) {
        return new Result<>(200, "成功", data);
    }

    public static <T> Result<T> error(String msg) {
        return new Result<>(500, msg, null);
    }

    public static <T> Result<T> error() {
        return new Result<>(500, "异常错误", null);
    }

    public static <T> Result<T> create(Integer code, String msg, T data) {
        return new Result<>(code, msg, data);
    }

    public static <T> Result<T> create(Integer code, String msg) {
        return new Result<>(code, msg, null);
    }
}