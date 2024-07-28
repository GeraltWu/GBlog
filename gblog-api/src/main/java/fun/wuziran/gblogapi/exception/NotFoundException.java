package fun.wuziran.gblogapi.exception;

import org.springframework.web.bind.annotation.RestControllerAdvice;

/**
 * @Description 404 Not Found Exception 找不到资源异常
 * @Author Geralt
 * @Date 2024/7/17
 */

public class NotFoundException extends RuntimeException {
    public NotFoundException() {
    }

    public NotFoundException(String message) {
        super(message);
    }

    public NotFoundException(String message, Throwable cause) {
        super(message, cause);
    }
}
