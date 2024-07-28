package fun.wuziran.gblogapi.exception;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */
public class PersistenceException extends RuntimeException {
    public PersistenceException() {
    }

    public PersistenceException(String message) {
        super(message);
    }

    public PersistenceException(String message, Throwable cause) {
        super(message, cause);
    }
}
