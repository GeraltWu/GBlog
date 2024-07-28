package fun.wuziran.gblogapi.model.vo;

import lombok.Data;

/**
 * @Description 用来封装响应结果
 * @Author Geralt
 * @Date 2024/7/17
 */

@Data
public class Result {
    private Integer code; // 响应状态码
    private String msg; // 响应消息
    private Object data; // 响应数据

    private Result(Integer code, String msg) {
        this.code = code;
        this.msg = msg;
        this.data = null;
    }

    private Result(Integer code, String msg, Object data) {
        this.code = code;
        this.msg = msg;
        this.data = data;
    }

    /**
     * 为每种传参方式提供相应的方法，返回的都是 Result 对象
     */

    public static Result ok(String msg, Object data) {
        return new Result(200, msg, data);
    }

    public static Result ok(String msg) {
        return new Result(200, msg);
    }

    public static Result error(String msg) {
        return new Result(500, msg);
    }

    public static Result error() {
        return new Result(500, "异常错误");
    }

    /**
     * 提供创建响应对象的方法，可以自定义 code 和 msg
     */
    public static Result create(Integer code, String msg, Object data) {
        return new Result(code, msg, data);
    }

    public static Result create(Integer code, String msg) {
        return new Result(code, msg);
    }
}
